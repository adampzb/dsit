# Angular Version-by-Version Migration Guide (v10 → v19)

This guide provides a detailed, step-by-step migration path from Angular 10 to Angular 19, with specific code changes required for each version to prevent breaking changes.

## 🎯 Migration Strategy

1. **Incremental Updates**: Migrate one major version at a time
2. **Test After Each Step**: Run comprehensive tests after each version update
3. **Code Refactoring**: Update deprecated APIs and patterns as you go
4. **Dependency Management**: Update related libraries at each step

## 📋 Pre-Migration Checklist

- [ ] Backup your current project
- [ ] Ensure all tests are passing in Angular 10
- [ ] Update Node.js to LTS version (v18+ recommended)
- [ ] Clean up `node_modules` and reinstall dependencies
- [ ] Document current build configuration

## 🚀 Version-by-Version Migration

### Phase 1: Angular 10 → Angular 11

#### 1. Update Angular Core
```bash
ng update @angular/core@11 @angular/cli@11
```

#### 2. Required Code Changes
- **Router**: Update `canLoad` guards to return `UrlTree | boolean` instead of `boolean | Observable<boolean>`
- **Forms**: Replace deprecated `ngModel` with `formControl` in reactive forms
- **HTTP**: Ensure all HTTP interceptors handle `HttpEvent` properly

#### 3. Dependency Updates
```bash
npm install rxjs@6.6.0 typescript@4.0.8
```

#### 4. Testing
- Run `ng test` to ensure no breaking changes
- Check for deprecation warnings in console

### Phase 2: Angular 11 → Angular 12

#### 1. Update Angular Core
```bash
ng update @angular/core@12 @angular/cli@12
```

#### 2. Required Code Changes
- **Ivy Engine**: Ensure all components are Ivy-compatible
  - Remove `metadata.json` files
  - Update `tsconfig.json`:
    ```json
    {
      "angularCompilerOptions": {
        "enableIvy": true
      }
    }
    ```
- **Legacy i18n**: Migrate from legacy i18n to new Ivy-based i18n
- **View Engine**: Remove View Engine specific code

#### 3. Dependency Updates
```bash
npm install rxjs@6.6.7 typescript@4.2.4
```

#### 4. Build Configuration
- Update `angular.json`:
  ```json
  {
    "projects": {
      "your-project": {
        "architect": {
          "build": {
            "options": {
              "aot": true,
              "buildOptimizer": true
            }
          }
        }
      }
    }
  }
  ```

### Phase 3: Angular 12 → Angular 13

#### 1. Update Angular Core
```bash
ng update @angular/core@13 @angular/cli@13
```

#### 2. Required Code Changes
- **RxJS 7.4**: Update RxJS operators
  - Replace `toPromise()` with `lastValueFrom()` or `firstValueFrom()`
  - Update deprecated operators
- **Forms**: Update `AbstractControl` usage
- **Router**: Update `NavigationExtras` usage

#### 3. Dependency Updates
```bash
npm install rxjs@7.4.0 typescript@4.4.4
```

#### 4. IE11 Support
- Update `polyfills.ts`:
  ```typescript
  // Remove IE11 polyfills if not needed
  // import 'core-js/es/symbol';
  // import 'core-js/es/object';
  ```

### Phase 4: Angular 13 → Angular 14

#### 1. Update Angular Core
```bash
ng update @angular/core@14 @angular/cli@14
```

#### 2. Required Code Changes
- **Standalone Components**: Start migrating to standalone components
  ```typescript
  @Component({
    standalone: true,
    imports: [CommonModule, RouterModule]
  })
  ```
- **Typed Forms**: Update to typed reactive forms
  ```typescript
  const form = new FormGroup({
    name: new FormControl<string>('', { nonNullable: true })
  });
  ```
- **Router**: Update `RouterLink` usage

#### 3. Dependency Updates
```bash
npm install rxjs@7.5.0 typescript@4.7.4
```

#### 4. CLI Changes
- Update `angular.json`:
  ```json
  {
    "cli": {
      "analytics": false
    }
  }
  ```

### Phase 5: Angular 14 → Angular 15

#### 1. Update Angular Core
```bash
ng update @angular/core@15 @angular/cli@15
```

#### 2. Required Code Changes
- **Stable Standalone Components**: Complete migration to standalone components
- **Legacy NgModule**: Remove `NgModule` where possible
- **Router**: Update `RouterModule.forRoot()` configuration
- **HTTP**: Update `HttpClient` interceptors

#### 3. Dependency Updates
```bash
npm install rxjs@7.8.0 typescript@4.8.4
```

#### 4. Build Optimization
- Update `angular.json`:
  ```json
  {
    "optimization": {
      "scripts": true,
      "styles": true,
      "fonts": true
    }
  }
  ```

### Phase 6: Angular 15 → Angular 16

#### 1. Update Angular Core
```bash
ng update @angular/core@16 @angular/cli@16
```

#### 2. Required Code Changes
- **Signals**: Start using Angular Signals
  ```typescript
  import { signal, computed, effect } from '@angular/core';
  
  const count = signal(0);
  const double = computed(() => count() * 2);
  ```
- **New Reactivity Model**: Update change detection strategies
- **Router**: Update `RouterLinkActive` usage

#### 3. Dependency Updates
```bash
npm install rxjs@7.8.0 typescript@4.9.5
```

#### 4. Vite Integration (Optional)
- Consider migrating to Vite for development server

### Phase 7: Angular 16 → Angular 17

#### 1. Update Angular Core
```bash
ng update @angular/core@17 @angular/cli@17
```

#### 2. Required Code Changes
- **New Control Flow**: Update templates to use new control flow
  ```html
  <!-- Old -->
  <div *ngIf="condition">Content</div>
  
  <!-- New -->
  @if (condition) {
    <div>Content</div>
  }
  ```
- **Deferrable Views**: Implement deferrable views
  ```html
  @defer {
    <heavy-component />
  }
  ```
- **Signals**: Complete migration to Signals-based reactivity

#### 3. Dependency Updates
```bash
npm install rxjs@7.8.0 typescript@5.2.2
```

#### 4. Build Configuration
- Update `angular.json` for new build system

### Phase 8: Angular 17 → Angular 18

#### 1. Update Angular Core
```bash
ng update @angular/core@18 @angular/cli@18
```

#### 2. Required Code Changes
- **Zoneless Change Detection**: Prepare for zoneless applications
- **New SSR**: Update server-side rendering configuration
- **Hydration**: Implement hydration for SSR apps

#### 3. Dependency Updates
```bash
npm install rxjs@7.8.0 typescript@5.3.3
```

### Phase 9: Angular 18 → Angular 19

#### 1. Update Angular Core
```bash
ng update @angular/core@19 @angular/cli@19
```

#### 2. Required Code Changes
- **Finalize Signals**: Complete Signals migration
- **New DevTools**: Update debugging approach
- **Performance Optimizations**: Implement latest optimizations

#### 3. Dependency Updates
```bash
npm install rxjs@7.8.0 typescript@5.4.5
```

## 🔧 Post-Migration Tasks

### 1. Testing Strategy
- [ ] Run unit tests: `ng test`
- [ ] Run e2e tests: `ng e2e`
- [ ] Test all major user flows manually
- [ ] Performance testing

### 2. Code Quality
- [ ] Update ESLint configuration
- [ ] Run `ng lint --fix`
- [ ] Update Prettier configuration
- [ ] Run code formatting

### 3. Build Optimization
- [ ] Update production build configuration
- [ ] Test tree-shaking effectiveness
- [ ] Optimize bundle size
- [ ] Implement lazy loading where missing

### 4. Documentation
- [ ] Update README with new Angular version
- [ ] Document breaking changes for team
- [ ] Update setup instructions
- [ ] Document new features used

## 🛠 Tools and Resources

### Migration Tools
- `ng update` - Official Angular update tool
- `ng generate` - For creating standalone components
- `ng lint` - For code quality checks

### Helpful Commands
```bash
# Check for deprecated APIs
ng lint --fix

# Analyze bundle size
ng build --stats-json

# Check Angular version
ng version
```

### Official Resources
- [Angular Update Guide](https://update.angular.io/)
- [Angular Migration Documentation](https://angular.io/guide/update-to-latest-version)
- [Angular Signals Documentation](https://angular.io/guide/signals)
- [Standalone Components Guide](https://angular.io/guide/standalone-components)

## 📊 Migration Progress Tracker

| Version | Status | Date Completed | Notes |
|---------|--------|----------------|-------|
| 10 → 11 | ⬜️ | - | - |
| 11 → 12 | ⬜️ | - | - |
| 12 → 13 | ⬜️ | - | - |
| 13 → 14 | ⬜️ | - | - |
| 14 → 15 | ⬜️ | - | - |
| 15 → 16 | ⬜️ | - | - |
| 16 → 17 | ⬜️ | - | - |
| 17 → 18 | ⬜️ | - | - |
| 18 → 19 | ⬜️ | - | - |

## ⚠️ Common Pitfalls and Solutions

### 1. Dependency Conflicts
**Problem**: Version mismatches between Angular and third-party libraries
**Solution**: Use `npm ls` to check dependency tree, update conflicting packages

### 2. Breaking Changes in RxJS
**Problem**: RxJS operator deprecations
**Solution**: Use `rxjs-compat` temporarily, then refactor

### 3. Template Errors
**Problem**: Template syntax changes between versions
**Solution**: Run `ng lint` and fix template errors systematically

### 4. Build Failures
**Problem**: Build fails after version update
**Solution**: Check `angular.json`, update build configuration

### 5. Test Failures
**Problem**: Tests fail after migration
**Solution**: Update test setup, mock new APIs properly

## 🎓 Best Practices for Smooth Migration

1. **Small, Incremental Steps**: Migrate one version at a time
2. **Comprehensive Testing**: Test thoroughly after each step
3. **Document Changes**: Keep track of what was changed and why
4. **Team Communication**: Keep team informed about migration progress
5. **Backup Regularly**: Create backups before each major step
6. **Use Git Tags**: Tag each successful version migration
7. **Monitor Performance**: Check bundle size and performance after each step

---

*Created for DSIT Angular migration project*
*Version-by-version migration guide for Angular 10 → 19*
*Last updated: 2024*