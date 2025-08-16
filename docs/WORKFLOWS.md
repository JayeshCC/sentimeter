# 🔄 Workflow Documentation

This document describes the automated workflows set up for the Sentimeter project to ensure code quality, security, and documentation standards.

## 📋 Overview

We use GitHub Actions to automate various quality checks and security scans. All workflows are designed to run efficiently and provide clear feedback to contributors.

## 🛡️ Security Workflows

### Security Scan (`security-scan.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` branch  
- Daily scheduled run at 2 AM UTC

**Jobs:**

#### 1. CodeQL Security Analysis
- **Purpose**: Static analysis to find security vulnerabilities
- **Languages**: JavaScript (expandable to Python, Java, etc.)
- **Features**: 
  - Enhanced security queries
  - Security-and-quality rule sets
  - Automatic vulnerability detection

#### 2. Secret Scanning
- **Purpose**: Detect accidentally committed secrets
- **Tool**: TruffleHog
- **Scope**: Full repository history
- **Mode**: Verified secrets only (reduces false positives)

#### 3. Dependency Vulnerability Scan
- **Purpose**: Check for known vulnerabilities in dependencies
- **Tools**: 
  - `npm audit` (built-in Node.js security)
  - Snyk (when token available)
- **Threshold**: Medium severity and above

#### 4. Documentation Security Check
- **Purpose**: Validate documentation for security issues
- **Checks**:
  - Hardcoded secrets in docs
  - Insecure HTTP URLs (except localhost)
  - Presence of SECURITY.md file

#### 5. Link Security Validation
- **Purpose**: Ensure all links in documentation are valid
- **Tool**: markdown-link-check
- **Features**: Timeout handling, retry logic

## 📚 Documentation Quality Workflows

### Documentation Quality (`docs-quality.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` branch (when markdown files change)

**Jobs:**

#### 1. Markdown Linting
- **Purpose**: Ensure consistent markdown formatting
- **Tool**: markdownlint-cli
- **Rules**: 
  - ATX-style headers
  - 120 character line limit
  - Consistent indentation
  - Allow HTML tags and multiple headers

#### 2. Spell Check
- **Purpose**: Catch typos and spelling errors
- **Tool**: cspell
- **Features**:
  - Technical dictionary included
  - Project-specific word list
  - Ignores code blocks and technical terms

#### 3. Link Validation
- **Purpose**: Ensure all links work correctly
- **Tool**: markdown-link-check
- **Features**:
  - Configurable timeouts
  - Retry on 429 errors
  - Ignores localhost links

#### 4. Documentation Structure Validation
- **Purpose**: Ensure required documentation files exist
- **Checks**:
  - README.md with proper sections
  - LICENSE file
  - CONTRIBUTING.md
  - SECURITY.md

#### 5. Documentation Metrics
- **Purpose**: Provide insights into documentation coverage
- **Metrics**:
  - File count
  - Word count
  - Line count
  - Code example count

## ⚙️ Workflow Configuration

### Security Configuration

The security workflows are configured to:
- **Fail fast**: Stop on critical security issues
- **Allow warnings**: Non-critical issues don't fail the build
- **Schedule regular scans**: Daily scans catch new vulnerabilities
- **Provide detailed reports**: Clear summaries in GitHub

### Documentation Configuration

The documentation workflows:
- **Run on changes**: Only when markdown files change
- **Provide metrics**: Track documentation quality over time
- **Generate summaries**: Clear results for reviewers
- **Allow customization**: Easy to adjust rules and thresholds

## 🔧 Setting Up Workflows

### Prerequisites

1. **Repository secrets** (optional but recommended):
   - `SNYK_TOKEN`: For enhanced dependency scanning
   - Any other security scanning tokens

2. **Permissions**: 
   - Workflows need `security-events: write` for security scans
   - `contents: read` for accessing repository files
   - `pull-requests: write` for commenting on PRs

### Customization

#### Adding New Languages
To add support for additional programming languages:

1. Update `.github/workflows/security-scan.yml`
2. Add language to the `matrix.language` array
3. Ensure CodeQL supports the language

```yaml
matrix:
  language: [ 'javascript', 'python', 'java' ]
```

#### Adjusting Security Thresholds

To change security severity thresholds:

1. Modify the `--audit-level` in npm audit
2. Update Snyk `--severity-threshold`
3. Adjust custom security checks

#### Customizing Documentation Rules

To modify documentation quality rules:

1. Edit `.markdownlint.json` configuration
2. Update `cspell.json` word list
3. Modify link check patterns

## 📊 Monitoring and Maintenance

### Regular Tasks

1. **Review workflow results** weekly
2. **Update security tools** monthly
3. **Refresh word lists** as needed
4. **Check for new vulnerabilities** via scheduled scans

### Troubleshooting

#### Common Issues

1. **False positive secrets**: Update TruffleHog exclusions
2. **Link check failures**: Add to ignore patterns if legitimate
3. **Spell check errors**: Add technical terms to word list
4. **Dependency issues**: Update vulnerable packages

#### Getting Help

- Check workflow logs for detailed error messages
- Review the GitHub Actions documentation
- Contact the development team for complex issues

## 🚀 Benefits

### For Contributors
- **Immediate feedback** on security and quality issues
- **Consistent standards** across all contributions
- **Learning opportunity** through automated suggestions

### for Maintainers
- **Automated quality gates** reduce manual review time
- **Security confidence** through comprehensive scanning
- **Documentation quality** ensures good user experience

### For Users
- **Secure codebase** through continuous monitoring
- **High-quality documentation** that's accurate and helpful
- **Reliable software** with fewer bugs and vulnerabilities

## 📈 Future Enhancements

Planned improvements to the workflow system:

1. **Performance testing** workflows
2. **Accessibility testing** for documentation
3. **Automated security updates** for dependencies
4. **Integration testing** with external services
5. **Release automation** with security validation

---

**For questions about workflows, please create an issue or contact the development team.**