#!/usr/bin/env python3
"""
Comprehensive Security Scanner for sentimeter Repository
This script performs various security checks and generates a security report.
"""

import os
import re
import json
import subprocess
import hashlib
from datetime import datetime
from pathlib import Path

class SecurityScanner:
    def __init__(self, repo_path="."):
        self.repo_path = Path(repo_path)
        self.findings = []
        self.info = []
        
    def log_finding(self, severity, category, description, file_path=None, line_number=None):
        """Log a security finding"""
        finding = {
            "severity": severity,
            "category": category,
            "description": description,
            "file_path": file_path,
            "line_number": line_number,
            "timestamp": datetime.now().isoformat()
        }
        self.findings.append(finding)
        
    def log_info(self, message):
        """Log informational message"""
        self.info.append(message)
        
    def scan_secrets(self):
        """Scan for potential secrets and credentials"""
        print("🔍 Scanning for secrets and credentials...")
        
        # Common secret patterns
        patterns = {
            "API Key": r"(?i)(api[_-]?key|apikey)\s*[:=]\s*['\"]?([a-zA-Z0-9_-]{16,})['\"]?",
            "Password": r"(?i)(password|pwd|pass)\s*[:=]\s*['\"]?([^\s'\";]{8,})['\"]?",
            "Token": r"(?i)(token|auth[_-]?token)\s*[:=]\s*['\"]?([a-zA-Z0-9_-]{16,})['\"]?",
            "Secret": r"(?i)(secret|private[_-]?key)\s*[:=]\s*['\"]?([a-zA-Z0-9_-]{16,})['\"]?",
            "AWS Access Key": r"AKIA[0-9A-Z]{16}",
            "GitHub Token": r"ghp_[a-zA-Z0-9]{36}|github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}",
            "JWT Token": r"eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*",
            "Private Key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
            "SSH Key": r"ssh-rsa AAAAB3NzaC1yc2E",
        }
        
        for file_path in self.repo_path.rglob("*"):
            if file_path.is_file() and not self._is_binary(file_path) and not self._should_skip_file(file_path):
                try:
                    content = file_path.read_text(encoding='utf-8', errors='ignore')
                    # Skip scanning certain files that contain security patterns as configuration
                    if file_path.name in ["security_scan.py", ".gitleaks.toml", "SECURITY_REPORT.md", "security_report.json"]:
                        continue
                        
                    for pattern_name, pattern in patterns.items():
                        matches = re.finditer(pattern, content, re.MULTILINE)
                        for match in matches:
                            line_number = content[:match.start()].count('\n') + 1
                            self.log_finding(
                                "HIGH", 
                                "Potential Secret", 
                                f"Potential {pattern_name} found",
                                str(file_path.relative_to(self.repo_path)),
                                line_number
                            )
                except Exception as e:
                    self.log_info(f"Could not scan {file_path}: {e}")
                    
    def scan_git_history(self):
        """Scan git history for potential security issues"""
        print("🔍 Scanning git history...")
        
        try:
            # Check for large files in history
            result = subprocess.run(
                ["git", "rev-list", "--objects", "--all"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                large_files = []
                for line in lines:
                    if line:
                        parts = line.split(' ', 1)
                        if len(parts) == 2:
                            obj_hash, filename = parts
                            try:
                                size_result = subprocess.run(
                                    ["git", "cat-file", "-s", obj_hash],
                                    cwd=self.repo_path,
                                    capture_output=True,
                                    text=True
                                )
                                if size_result.returncode == 0:
                                    size = int(size_result.stdout.strip())
                                    if size > 1024 * 1024:  # 1MB
                                        large_files.append((filename, size))
                            except:
                                pass
                                
                for filename, size in large_files:
                    self.log_finding(
                        "MEDIUM",
                        "Large File",
                        f"Large file in git history: {filename} ({size} bytes)",
                        filename
                    )
                    
            # Check for sensitive file patterns in history
            sensitive_patterns = [
                r"\.env$",
                r"\.key$", 
                r"\.pem$",
                r"id_rsa$",
                r"\.p12$",
                r"\.jks$",
                r"config\.json$",
                r"secrets\..*",
                r"\.aws/",
                r"\.ssh/"
            ]
            
            for pattern in sensitive_patterns:
                result = subprocess.run(
                    ["git", "log", "--all", "--full-history", "--name-only", "--pretty=format:", "--", f"*{pattern}"],
                    cwd=self.repo_path,
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    files = set(result.stdout.strip().split('\n'))
                    for file in files:
                        if file:
                            self.log_finding(
                                "HIGH",
                                "Sensitive File in History",
                                f"Potentially sensitive file found in git history: {file}",
                                file
                            )
                            
        except Exception as e:
            self.log_info(f"Error scanning git history: {e}")
            
    def scan_file_permissions(self):
        """Check file permissions for security issues"""
        print("🔍 Checking file permissions...")
        
        for file_path in self.repo_path.rglob("*"):
            if file_path.is_file() and not self._should_skip_file(file_path):
                try:
                    stat = file_path.stat()
                    mode = oct(stat.st_mode)[-3:]
                    
                    # Check for world-writable files
                    if mode[-1] in ['2', '3', '6', '7']:
                        self.log_finding(
                            "MEDIUM",
                            "File Permissions",
                            f"World-writable file: {file_path}",
                            str(file_path.relative_to(self.repo_path))
                        )
                        
                    # Check for executable files that shouldn't be
                    if mode[0] in ['7', '5', '3', '1'] and file_path.suffix in ['.txt', '.md', '.json', '.yml', '.yaml']:
                        self.log_finding(
                            "LOW",
                            "File Permissions", 
                            f"Executable text file: {file_path}",
                            str(file_path.relative_to(self.repo_path))
                        )
                        
                except Exception as e:
                    self.log_info(f"Could not check permissions for {file_path}: {e}")
                    
    def scan_dependencies(self):
        """Scan for known vulnerable dependencies"""
        print("🔍 Scanning dependencies...")
        
        dependency_files = [
            "package.json", "package-lock.json",
            "requirements.txt", "Pipfile", "Pipfile.lock",
            "Gemfile", "Gemfile.lock",
            "composer.json", "composer.lock",
            "go.mod", "go.sum",
            "pom.xml", "build.gradle"
        ]
        
        found_files = []
        for dep_file in dependency_files:
            dep_path = self.repo_path / dep_file
            if dep_path.exists():
                found_files.append(dep_file)
                self.log_info(f"Found dependency file: {dep_file}")
                
        if not found_files:
            self.log_info("No dependency files found")
            
    def scan_configuration_files(self):
        """Scan configuration files for security issues"""
        print("🔍 Scanning configuration files...")
        
        config_patterns = [
            "*.conf", "*.config", "*.cfg", "*.ini",
            "*.env", "*.env.*", 
            "docker-compose.yml", "Dockerfile",
            ".github/**/*.yml", ".github/**/*.yaml",
            "*.json", "*.yaml", "*.yml"
        ]
        
        for pattern in config_patterns:
            for config_file in self.repo_path.glob(pattern):
                if config_file.is_file():
                    self.log_info(f"Found configuration file: {config_file.relative_to(self.repo_path)}")
                    
                    try:
                        content = config_file.read_text(encoding='utf-8', errors='ignore')
                        
                        # Check for hardcoded IPs
                        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
                        ips = re.findall(ip_pattern, content)
                        for ip in ips:
                            if not ip.startswith(('127.', '0.0.0.0', '192.168.', '10.', '172.')):
                                self.log_finding(
                                    "MEDIUM",
                                    "Hardcoded IP",
                                    f"Hardcoded public IP address: {ip}",
                                    str(config_file.relative_to(self.repo_path))
                                )
                                
                        # Check for debug settings
                        if re.search(r'(?i)(debug|verbose)\s*[:=]\s*(true|1|on)', content):
                            self.log_finding(
                                "LOW",
                                "Debug Configuration",
                                "Debug mode enabled in configuration",
                                str(config_file.relative_to(self.repo_path))
                            )
                            
                    except Exception as e:
                        self.log_info(f"Could not scan configuration file {config_file}: {e}")
                        
    def _is_binary(self, file_path):
        """Check if file is binary"""
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(1024)
                return b'\0' in chunk
        except:
            return True
            
    def _should_skip_file(self, file_path):
        """Check if file should be skipped"""
        skip_patterns = [
            '.git/',
            '__pycache__/',
            'node_modules/',
            '.venv/',
            'venv/',
            '.DS_Store',
            '*.pyc',
            '*.pyo',
            '*.so',
            '*.dll',
            '*.exe'
        ]
        
        file_str = str(file_path)
        for pattern in skip_patterns:
            if pattern in file_str or file_str.endswith(pattern.replace('*', '')):
                return True
        return False
        
    def generate_report(self):
        """Generate security report"""
        print("\n📋 Generating security report...")
        
        report = {
            "scan_timestamp": datetime.now().isoformat(),
            "repository_path": str(self.repo_path),
            "summary": {
                "total_findings": len(self.findings),
                "high_severity": len([f for f in self.findings if f["severity"] == "HIGH"]),
                "medium_severity": len([f for f in self.findings if f["severity"] == "MEDIUM"]),
                "low_severity": len([f for f in self.findings if f["severity"] == "LOW"])
            },
            "findings": self.findings,
            "info": self.info
        }
        
        # Save JSON report
        report_file = self.repo_path / "security_report.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
            
        # Generate markdown report
        self._generate_markdown_report(report)
        
        return report
        
    def _generate_markdown_report(self, report):
        """Generate markdown security report"""
        md_content = f"""# Security Analysis Report

**Generated:** {report['scan_timestamp']}  
**Repository:** {report['repository_path']}

## Summary

- **Total Findings:** {report['summary']['total_findings']}
- **High Severity:** {report['summary']['high_severity']}
- **Medium Severity:** {report['summary']['medium_severity']}  
- **Low Severity:** {report['summary']['low_severity']}

## Findings

"""
        
        if not self.findings:
            md_content += "✅ **No security issues found!**\n\n"
        else:
            for finding in self.findings:
                md_content += f"### {finding['severity']} - {finding['category']}\n\n"
                md_content += f"**Description:** {finding['description']}\n\n"
                if finding['file_path']:
                    md_content += f"**File:** `{finding['file_path']}`\n\n"
                if finding['line_number']:
                    md_content += f"**Line:** {finding['line_number']}\n\n"
                md_content += "---\n\n"
                
        md_content += "## Information\n\n"
        for info in self.info:
            md_content += f"- {info}\n"
            
        md_content += """
## Security Recommendations

### Immediate Actions
1. 🔐 Never commit secrets, API keys, or credentials to version control
2. 📁 Add sensitive files to `.gitignore` 
3. 🔍 Use tools like `git-secrets` or `truffleHog` to scan for secrets
4. 📝 Implement pre-commit hooks for security scanning

### Best Practices
1. 🛡️ Use environment variables for sensitive configuration
2. 🔑 Rotate credentials regularly
3. 📊 Implement dependency scanning (e.g., GitHub Dependabot)
4. 🏗️ Use infrastructure as code with security scanning
5. 🔒 Enable branch protection rules
6. 📋 Regular security audits and penetration testing

### Security Tools to Consider
- **Static Analysis:** SonarQube, CodeQL, Bandit (Python)
- **Dependency Scanning:** Snyk, OWASP Dependency Check
- **Secret Scanning:** GitLeaks, TruffleHog, git-secrets
- **Container Security:** Trivy, Clair, Docker Bench
- **Infrastructure:** Checkov, Terraform Compliance

"""
        
        report_file = self.repo_path / "SECURITY_REPORT.md"
        with open(report_file, 'w') as f:
            f.write(md_content)
            
    def run_full_scan(self):
        """Run all security scans"""
        print("🚀 Starting comprehensive security scan...\n")
        
        self.scan_secrets()
        self.scan_git_history()
        self.scan_file_permissions()
        self.scan_dependencies()
        self.scan_configuration_files()
        
        report = self.generate_report()
        
        print(f"\n✅ Security scan completed!")
        print(f"📊 Found {report['summary']['total_findings']} issues")
        print(f"📁 Reports saved to: security_report.json and SECURITY_REPORT.md")
        
        return report

if __name__ == "__main__":
    scanner = SecurityScanner()
    scanner.run_full_scan()