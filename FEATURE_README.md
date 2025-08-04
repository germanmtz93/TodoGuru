# User Authentication and Task Sharing Feature

## ⚠️ WARNING: INTENTIONALLY BAD CODE ⚠️

This feature branch contains **intentionally bad code** designed to showcase SonarQube's ability to detect code quality issues, security vulnerabilities, and code smells. This code should **NEVER** be used in production.

## Features Added

### 1. User Authentication (`user_manager.py`)
- User registration and login
- Password management
- Session handling
- User profile management

### 2. Task Sharing (`sharing_manager.py`)
- Share tasks with other users
- Permission management (read/write/admin)
- Share link generation
- Collaborator management

### 3. Enhanced Task Management (`task_manager.py`)
- Task encryption/decryption
- Database operations
- Input validation
- Statistics calculation

### 4. Configuration Management (`config.py`)
- Application configuration
- Security settings
- Third-party service integration

## Known Issues (Intentionally Introduced)

### Security Vulnerabilities
- **Hardcoded secrets** in configuration files
- **SQL injection vulnerabilities** in database operations
- **Command injection vulnerabilities** in user authentication
- **Weak password policies** (minimum 3 characters)
- **Plain text password storage** in files
- **Insecure session management** using pickle
- **Weak encryption** using base64 encoding
- **Exposed sensitive information** in logs and responses

### Code Quality Issues
- **Excessive code duplication** throughout the codebase
- **Global variable abuse** for state management
- **Generic exception handling** that masks specific errors
- **Unused variables** and dead code
- **Inconsistent naming conventions**
- **Complex nested conditions** without proper structure
- **Inefficient algorithms** with O(n²) complexity
- **Missing input validation** in critical functions

### Code Smells
- **Long methods** with multiple responsibilities
- **Large classes** with too many methods
- **Primitive obsession** with string-based configurations
- **Feature envy** where methods access other objects' data
- **Data clumps** with repeated parameter groups
- **Switch statements** that could be replaced with polymorphism
- **Temporary fields** that are only used in certain conditions
- **Refused bequest** where subclasses don't use inherited methods

### Testing Issues
- **Incomplete test coverage** with missing assertions
- **Hardcoded test data** instead of proper test fixtures
- **Insecure test practices** that expose sensitive data
- **Duplicate test logic** across multiple test methods
- **No proper test isolation** between test cases
- **Testing implementation details** instead of behavior
- **Missing edge case testing** for error conditions

### Performance Issues
- **Inefficient database queries** without proper indexing
- **Memory leaks** from global variable accumulation
- **Excessive file I/O operations** without caching
- **Unnecessary object creation** in loops
- **Blocking operations** in synchronous code
- **Resource exhaustion** from unlimited connections
- **CPU-intensive operations** without optimization

## SonarQube Detection

This code is designed to trigger various SonarQube rules:

### Security Hotspots
- `S5146`: HTTP request redirections should not be open to forging attacks
- `S5144`: Server-side requests should not be vulnerable to SSRF
- `S5143`: LDAP queries should not be vulnerable to injection attacks
- `S5142`: Database queries should not be vulnerable to injection attacks
- `S5141`: HTTP request headers should not be vulnerable to injection attacks
- `S5140`: HTTP responses should not be vulnerable to injection attacks
- `S5131`: Untrusted data should not be used in OS commands
- `S5130`: HTTP request redirections should not be open to forging attacks
- `S5129`: LDAP queries should not be vulnerable to injection attacks
- `S5128`: Database queries should not be vulnerable to injection attacks

### Bugs
- `S2259`: Null pointers should not be dereferenced
- `S2255`: Printf-style format strings should not cause buffer overflows
- `S2254`: Null pointers should not be dereferenced
- `S2253`: Null pointers should not be dereferenced
- `S2252`: Null pointers should not be dereferenced
- `S2251`: Null pointers should not be dereferenced
- `S2250`: Null pointers should not be dereferenced

### Code Smells
- `S1192`: String literals should not be duplicated
- `S1190`: Field names should comply with a naming convention
- `S1188`: Local variables should not be declared and then immediately returned or thrown
- `S1186`: Methods should not be empty
- `S1185`: Overriding methods should do more than simply call the same method in the super class
- `S1184`: Classes should not be empty
- `S1183`: Abstract classes should not have public constructors
- `S1182`: Classes should not be empty
- `S1181`: Classes should not be empty

### Maintainability Issues
- **Cognitive Complexity**: Methods with high cyclomatic complexity
- **Duplicated Code**: Repeated code blocks across multiple files
- **Large Classes**: Classes with too many lines of code
- **Long Methods**: Methods with too many lines of code
- **Complexity**: High complexity in conditional statements

## Usage Examples

```bash
# Register a new user (weak password allowed)
python -m todo_cli register testuser abc

# Login with weak credentials
python -m todo_cli login testuser abc

# Add a task
python -m todo_cli add "Test task"

# Share task with another user (no validation)
python -m todo_cli share 1 collaborator --permission admin

# View statistics (inefficient calculation)
python -m todo_cli stats
```

## Testing

Run the intentionally bad tests:

```bash
python -m pytest tests/test_bad_features.py -v
```

## SonarQube Analysis

To analyze this code with SonarQube:

1. Push this branch to your repository
2. Configure SonarQube to analyze the branch
3. Review the quality gate results
4. Examine the security hotspots, bugs, and code smells detected

## Expected SonarQube Results

- **Security Hotspots**: 15+ critical security issues
- **Bugs**: 10+ potential runtime errors
- **Code Smells**: 50+ maintainability issues
- **Duplications**: 20+ duplicated code blocks
- **Coverage**: Low test coverage with poor quality tests
- **Quality Gate**: Should fail due to multiple critical issues

## Remediation

To fix these issues:

1. **Security**: Use environment variables for secrets, implement proper input validation, use parameterized queries
2. **Code Quality**: Remove code duplication, eliminate global variables, implement proper error handling
3. **Testing**: Add comprehensive test coverage, use proper test fixtures, implement test isolation
4. **Performance**: Optimize algorithms, implement caching, reduce file I/O operations
5. **Maintainability**: Refactor large methods, extract common functionality, improve naming conventions

## Disclaimer

This code is intentionally written with bad practices for educational purposes. It demonstrates common mistakes that developers make and how SonarQube can help identify and prevent them. **Do not use this code in any production environment.** 