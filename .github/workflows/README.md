# GitHub Actions Workflows

This directory contains automated workflows for the Sentimeter project.

## 🔄 Active Workflows

| Workflow | Purpose | Trigger | Status |
|----------|---------|---------|--------|
| [Security Scan](./security-scan.yml) | Security vulnerability detection | Push, PR, Schedule | ![Security](https://github.com/JayeshCC/sentimeter/workflows/Security%20Scan/badge.svg) |
| [Documentation Quality](./docs-quality.yml) | Documentation linting and validation | Push, PR (docs changes) | ![Docs](https://github.com/JayeshCC/sentimeter/workflows/Documentation%20Quality/badge.svg) |

## 📋 Workflow Details

### Security Scan
- **CodeQL Analysis**: Static security analysis
- **Secret Scanning**: Detect committed secrets  
- **Dependency Check**: Vulnerability scanning
- **Documentation Security**: Check docs for security issues
- **Link Validation**: Ensure secure and valid links

### Documentation Quality  
- **Markdown Linting**: Format consistency
- **Spell Check**: Catch typos and errors
- **Link Check**: Validate all links work
- **Structure Validation**: Ensure required files exist
- **Metrics**: Track documentation coverage

## 🔧 Configuration

Workflows are configured to:
- Run automatically on code changes
- Provide detailed feedback in PR reviews
- Generate security and quality reports
- Fail on critical issues, warn on minor ones

## 📚 Documentation

For detailed information about workflows, see [WORKFLOWS.md](../WORKFLOWS.md).

## 🆘 Support

If workflows are failing:
1. Check the Actions tab for detailed logs
2. Review the workflow documentation
3. Create an issue if problems persist