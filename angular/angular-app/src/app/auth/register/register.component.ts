// register.component.ts

import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthenticationService } from '../authentication.service';
import { matchValidator } from 'src/app/validators/password-match.validator';
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent {
  registerForm: FormGroup;

  constructor(private fb: FormBuilder, private authService: AuthenticationService, private router: Router, private tokenService: TokenService, private snack: MatSnackBar) {
    this.registerForm = this.fb.group({
      username: ['', [Validators.required,
                      Validators.minLength(4),
                      Validators.maxLength(20),
                      Validators.pattern('^[a-zA-Z0-9_-]*$')]],
      password: ['', [Validators.required, 
                      Validators.minLength(8),
                      matchValidator('confirmPassword', true)]],
      confirmPassword: ['', [Validators.required, matchValidator('password')]],
      email: ['', [Validators.required, Validators.email]],
      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      birth_date: ['', Validators.required],
      user_profile: this.fb.group({
        weight: ['', Validators.required],
        height: ['', Validators.required]
      }),
      sex: ['', Validators.required],
      level_of_advancement: ['', Validators.required],
    });
  }

  onSubmit() {
    if (this.registerForm.valid) {
      this.authService.register(this.registerForm.value).subscribe({
        next: () => {
          let snack = this.snack.open('Successfully registered! Please log in now', 'Log in', { duration: 5000 });
          snack.afterDismissed().subscribe(() => {
            this.router.navigate(['/auth/login']);
          });
        },
        error: (error) => {
          if(error.error.username) {
            this.registerForm.controls['username'].setErrors({'backend': error.error.username});
          }
          if(error.error.email) {
            this.registerForm.controls['email'].setErrors({'backend': error.error.email});
          }
        },
      });
    } else {
      this.markFormGroupTouched(this.registerForm);
    }
  }

  private markFormGroupTouched(formGroup: FormGroup) {
    Object.values(formGroup.controls).forEach((control) => {
      control.markAsTouched();

      if (control instanceof FormGroup) {
        this.markFormGroupTouched(control);
      }
    });
  }
}
