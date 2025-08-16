# Security Policy

## Supported Versions

We take security seriously and actively maintain the security of the Sentimeter project. Security updates are provided for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We appreciate your efforts to responsibly disclose security vulnerabilities. Please follow these guidelines:

### 🔒 How to Report

**DO NOT** create a public issue for security vulnerabilities. Instead:

1. **Email us directly**: Send your report to `security@sentimeter.com`
2. **Include details**: Provide a clear description of the vulnerability
3. **Add steps to reproduce**: Help us understand and verify the issue
4. **Suggest a fix**: If you have ideas for fixing the issue, we'd love to hear them

### 📧 What to Include

Please include the following information in your report:

- **Description**: A clear description of the vulnerability
- **Impact**: What could an attacker achieve?
- **Steps to reproduce**: Detailed steps to reproduce the issue
- **Affected versions**: Which versions are affected?
- **Environment**: Browser, OS, or other relevant environment details
- **Supporting materials**: Screenshots, logs, or proof-of-concept code

### ⏱️ Response Timeline

We are committed to addressing security issues promptly:

- **Initial response**: Within 48 hours
- **Vulnerability assessment**: Within 7 days  
- **Fix timeline**: Critical issues within 14 days, others within 30 days
- **Public disclosure**: After fix is deployed and users have time to update

### 🛡️ Security Best Practices for Users

To help keep your implementation secure:

#### API Security
- ✅ **Never expose API keys** in client-side code or public repositories
- ✅ **Use HTTPS only** for all API requests in production
- ✅ **Implement rate limiting** to prevent abuse
- ✅ **Validate webhook signatures** when using webhooks
- ✅ **Use environment variables** for storing sensitive configuration

#### Data Protection
- ✅ **Sanitize input** before sending to the API
- ✅ **Don't log sensitive data** such as personal information
- ✅ **Use secure storage** for any cached results
- ✅ **Implement proper access controls** in your applications

#### Infrastructure Security
- ✅ **Keep dependencies updated** regularly
- ✅ **Use secure communication** (TLS 1.2 or higher)
- ✅ **Monitor for suspicious activity** in your logs
- ✅ **Implement proper error handling** to avoid information leakage

### 🏆 Recognition

We believe in recognizing security researchers who help us improve:

- **Hall of Fame**: Responsible disclosures will be credited in our security acknowledgments
- **Bug Bounty**: We may offer rewards for significant vulnerabilities (details to be announced)
- **Collaboration**: We're happy to work with researchers throughout the process

### 📝 Security Updates

Security updates and advisories will be published:

- **GitHub Security Advisories**: For all security issues affecting the codebase
- **Release Notes**: Security fixes will be clearly marked in release notes
- **Email notifications**: Critical security updates will be emailed to registered users

### 🔍 Security Testing

We regularly perform:

- **Automated security scanning** with CodeQL and other tools
- **Dependency vulnerability scanning** 
- **Regular security audits** of our codebase and infrastructure
- **Penetration testing** of our production systems

### 📞 Contact Information

- **Security Email**: security@sentimeter.com
- **General Support**: support@sentimeter.com
- **Documentation Issues**: Create an issue in this repository

### ⚖️ Legal

- We will not pursue legal action against researchers who follow this policy
- We request that you do not access user data or disrupt our services
- Please allow us reasonable time to address issues before public disclosure

---

**Thank you for helping keep Sentimeter and our users safe!** 🙏

Last updated: January 2024