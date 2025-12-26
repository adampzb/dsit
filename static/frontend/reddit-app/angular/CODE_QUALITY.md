# Angular Code Quality Guide

This guide explains the code quality setup for the Angular frontend, which provides similar functionality to Python's Flake8 and Black.

## Tools Overview

### 1. ESLint (Like Flake8)
- **Purpose**: Code linting and quality checks for TypeScript/JavaScript
- **Configuration**: `.eslintrc.json`
- **Angular-Specific**: Uses `@angular-eslint` for Angular best practices

### 2. Prettier (Like Black)
- **Purpose**: Code formatting for consistent style
- **Configuration**: `.prettierrc`
- **Features**: Auto-formats TypeScript, HTML, CSS, SCSS, JSON

### 3. Stylelint
- **Purpose**: CSS/SCSS linting and formatting
- **Configuration**: `.stylelintrc.json`
- **Features**: Enforces CSS best practices

### 4. Husky + lint-staged
- **Purpose**: Pre-commit hooks for automatic code quality checks
- **Configuration**: `.husky/` and `.lintstagedrc.json`

## Available Scripts

```bash
# Run ESLint with auto-fix
npm run lint:eslint

# Run Stylelint with auto-fix
npm run lint:style

# Run Prettier formatting
npm run lint:prettier

# Run all linting and formatting
npm run lint:all

# Check code quality without fixing
npm run check

# Format all files
npm run format
```

## Pre-commit Hooks

The project uses Husky to automatically run code quality checks on staged files before each commit:

1. **ESLint** - Checks TypeScript and HTML files
2. **Stylelint** - Checks CSS and SCSS files  
3. **Prettier** - Formats all supported files

If any issues are found, the commit will be blocked until they're fixed.

## Migration from Angular 10 to 19

### Compatibility Notes

The current setup is designed to work with both Angular 10 and prepare for Angular 19:

- **ESLint**: Uses `@angular-eslint` v18 which supports Angular 10+
- **TypeScript**: Current TypeScript 4.0.2 will need to be updated to 5.2+ for Angular 19
- **RxJS**: Current RxJS 6.6.0 will need to be updated to 7.8+ for Angular 19

### Migration Steps

1. **Update Angular Core**:
   ```bash
   ng update @angular/core@19 @angular/cli@19
   ```

2. **Update TypeScript**:
   ```bash
   npm install typescript@5.2.2 --save-dev
   ```

3. **Update RxJS**:
   ```bash
   npm install rxjs@7.8.1
   ```

4. **Update ESLint**:
   ```bash
   npm install @angular-eslint/eslint-plugin@19 @angular-eslint/eslint-plugin-template@19 @angular-eslint/template-parser@19 --save-dev
   ```

## Configuration Details

### ESLint Rules

- **Component Selectors**: `app-*` prefix with kebab-case
- **Directive Selectors**: `app*` prefix with camelCase
- **Type Safety**: Warns about `any` type usage
- **Console Restrictions**: Only allows `console.warn` and `console.error`

### Prettier Rules

- **Line Length**: 100 characters
- **Indentation**: 2 spaces
- **Quotes**: Single quotes
- **Semicolons**: Required
- **Trailing Commas**: ES5 style

### Stylelint Rules

- **Quotes**: Single quotes
- **Hex Colors**: Lowercase with short notation
- **Indentation**: 2 spaces
- **Semicolons**: Required

## Editor Integration

### VS Code

Add these extensions:
- **ESLint**: `dbaeumer.vscode-eslint`
- **Prettier**: `esbenp.prettier-vscode`
- **Stylelint**: `stylelint.vscode-stylelint`

Add to VS Code settings:
```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "eslint.validate": ["typescript", "html"],
  "stylelint.validate": ["css", "scss"]
}
```

## Troubleshooting

### Common Issues

1. **ESLint not working**:
   - Run `npm install` to ensure all dependencies are installed
   - Check that TypeScript version matches your project

2. **Pre-commit hooks failing**:
   - Run `npm run lint:all` to fix all issues manually
   - Use `git commit --no-verify` to bypass hooks if needed

3. **Stylelint errors**:
   - Some CSS rules might need to be adjusted in `.stylelintrc.json`

## Best Practices

1. **Run checks locally** before committing
2. **Fix issues incrementally** rather than all at once
3. **Update configurations** as your project evolves
4. **Document exceptions** in the configuration files

## Angular 19 Migration Checklist

- [ ] Update Angular core packages to v19
- [ ] Update TypeScript to v5.2+
- [ ] Update RxJS to v7.8+
- [ ] Update @angular-eslint packages to v19
- [ ] Test all components with new Angular version
- [ ] Update any deprecated APIs
- [ ] Run full test suite after migration

This setup ensures your Angular codebase maintains high quality standards similar to your Python backend, making the migration from Angular 10 to 19 smoother and more maintainable.