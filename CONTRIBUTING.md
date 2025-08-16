# 🤝 Contributing to Sentimeter

Thank you for your interest in contributing to Sentimeter! We welcome contributions from the community and appreciate your help in making our sentiment analysis tool better.

## 🌟 How You Can Contribute

There are many ways to contribute to Sentimeter:

- **🐛 Report bugs** - Help us identify and fix issues
- **💡 Suggest features** - Share ideas for new functionality
- **📝 Improve documentation** - Help make our docs clearer and more comprehensive
- **🔧 Submit code** - Fix bugs or implement new features
- **🧪 Test** - Help us test new features and find edge cases
- **🌍 Translations** - Help make Sentimeter available in more languages

## 🚀 Getting Started

### Prerequisites

Before contributing, make sure you have:

- Git installed on your machine
- Node.js (version 14 or higher)
- npm or yarn package manager
- A GitHub account

### Setting Up Your Development Environment

1. **Fork the repository**
   ```bash
   # Go to https://github.com/JayeshCC/sentimeter and click "Fork"
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/sentimeter.git
   cd sentimeter
   ```

3. **Add the original repository as upstream**
   ```bash
   git remote add upstream https://github.com/JayeshCC/sentimeter.git
   ```

4. **Install dependencies**
   ```bash
   npm install
   ```

5. **Create a development branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📋 Contribution Guidelines

### Code Style

We follow these coding standards:

- **JavaScript/TypeScript**: Use ESLint configuration provided
- **Formatting**: Use Prettier for code formatting
- **Naming**: Use camelCase for variables and functions, PascalCase for classes
- **Comments**: Write clear, concise comments for complex logic

### Commit Messages

Follow the conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
git commit -m "feat(api): add batch sentiment analysis endpoint"
git commit -m "fix(parser): handle empty text input correctly"
git commit -m "docs(readme): update installation instructions"
```

### Pull Request Process

1. **Ensure your branch is up to date**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests and linting**
   ```bash
   npm test
   npm run lint
   ```

3. **Push your changes**
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request**
   - Go to GitHub and create a PR from your fork
   - Use the PR template provided
   - Include a clear description of your changes
   - Reference any related issues

5. **Respond to feedback**
   - Address any review comments
   - Update your PR as needed

## 🐛 Reporting Bugs

When reporting bugs, please include:

### Bug Report Template

```markdown
## Bug Description
A clear description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Enter text '...'
4. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., Windows 10, macOS 12.0]
- Browser: [e.g., Chrome 96, Firefox 95]
- Sentimeter Version: [e.g., 1.2.0]

## Additional Context
Any other relevant information, screenshots, or logs.
```

### Before Reporting

- Search existing issues to avoid duplicates
- Try to reproduce the bug consistently
- Gather relevant error messages or logs

## 💡 Suggesting Features

We love feature suggestions! Here's how to propose them:

### Feature Request Template

```markdown
## Feature Description
A clear description of the feature you'd like to see.

## Problem Statement
What problem does this feature solve?

## Proposed Solution
How would you like this feature to work?

## Alternatives Considered
Any alternative solutions you've considered.

## Additional Context
Any other relevant information, mockups, or examples.
```

### Feature Guidelines

- Features should align with Sentimeter's core mission
- Consider the impact on existing users
- Think about API design and backward compatibility
- Consider performance implications

## 📝 Documentation Contributions

Help us improve our documentation:

### What to Document

- **API changes** - Update API docs for new endpoints
- **New features** - Add usage examples and guides
- **Bug fixes** - Update docs if behavior changes
- **Tutorials** - Create helpful tutorials for common use cases

### Documentation Standards

- Use clear, simple language
- Include code examples where appropriate
- Test all code samples
- Use proper markdown formatting
- Include images/diagrams when helpful

## 🧪 Testing

### Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm test -- --grep "sentiment analysis"
```

### Writing Tests

- Write tests for all new features
- Include edge cases and error scenarios
- Use descriptive test names
- Follow the existing test structure

**Example Test:**

```javascript
describe('Sentiment Analysis', () => {
  it('should correctly identify positive sentiment', async () => {
    const text = 'I love this product!';
    const result = await analyzeSentiment(text);
    
    expect(result.sentiment).toBe('positive');
    expect(result.confidence).toBeGreaterThan(0.8);
  });
  
  it('should handle empty text gracefully', async () => {
    const text = '';
    
    await expect(analyzeSentiment(text))
      .rejects
      .toThrow('Text cannot be empty');
  });
});
```

## 🏷️ Issue Labels

We use these labels to organize issues:

- **bug** - Something isn't working
- **enhancement** - New feature or request
- **documentation** - Improvements to documentation
- **good first issue** - Good for newcomers
- **help wanted** - Extra attention is needed
- **question** - Further information is requested
- **wontfix** - This will not be worked on

## 🌍 Translation Guidelines

Help us make Sentimeter available in more languages:

### How to Contribute Translations

1. Check if your language is already supported
2. Copy the English language file
3. Translate all strings
4. Test with native speakers
5. Submit a pull request

### Translation Standards

- Use formal tone unless informal is more appropriate
- Keep technical terms consistent
- Consider cultural context
- Test UI layout with translated text

## 🎉 Recognition

Contributors are recognized in:

- **README.md** - Major contributors listed
- **Release notes** - Contributors mentioned in releases
- **GitHub** - Contributions visible on GitHub profiles
- **Community** - Shoutouts in community channels

## 📞 Getting Help

Need help contributing? Reach out:

- **GitHub Discussions** - Ask questions and discuss ideas
- **Discord Community** - Join our contributor chat
- **Email** - contributors@sentimeter.com
- **Documentation** - Check our contribution docs

## 📋 Development Workflow

### Typical Development Cycle

1. **Pick an issue** - Choose from our issue tracker
2. **Discuss approach** - Comment on the issue with your plan
3. **Create branch** - Follow our branching strategy
4. **Develop** - Write code following our guidelines
5. **Test** - Ensure all tests pass
6. **Document** - Update relevant documentation
7. **Submit PR** - Create a pull request
8. **Review** - Respond to feedback
9. **Merge** - Your contribution is merged!

### Branch Naming

Use descriptive branch names:

- `feature/add-emotion-detection`
- `fix/empty-text-handling`
- `docs/api-examples`
- `refactor/sentiment-engine`

### Code Review Process

All submissions require code review:

1. **Automated checks** - CI/CD runs tests and linting
2. **Peer review** - Other contributors review your code
3. **Maintainer review** - Core team provides final approval
4. **Merge** - Changes are merged into main branch

## 🏆 Becoming a Maintainer

Regular contributors may be invited to become maintainers:

### Maintainer Responsibilities

- Review pull requests
- Triage issues
- Help with releases
- Mentor new contributors
- Make architectural decisions

### How to Become a Maintainer

- Consistent quality contributions
- Help other contributors
- Demonstrate understanding of project goals
- Show commitment to the project

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment:

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Give constructive feedback
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing private information
- Unprofessional conduct

### Enforcement

Violations may result in:
- Warning
- Temporary ban
- Permanent ban

Report issues to: conduct@sentimeter.com

## 🎯 Contribution Ideas

Looking for ways to contribute? Try these:

### For Beginners
- Fix typos in documentation
- Add code examples
- Improve error messages
- Write tests for existing code

### For Experienced Developers
- Implement new ML models
- Optimize performance
- Add new API endpoints
- Improve accuracy algorithms

### For Designers
- Improve documentation layout
- Create diagrams and flowcharts
- Design better error pages
- Improve user experience

### For Writers
- Write tutorials and guides
- Improve existing documentation
- Create video content
- Write blog posts

---

**Thank you for contributing to Sentimeter! Together, we're building the best sentiment analysis tool possible. 🚀**

For questions about contributing, feel free to reach out to our community or open a discussion on GitHub.

**Happy coding! 💻✨**