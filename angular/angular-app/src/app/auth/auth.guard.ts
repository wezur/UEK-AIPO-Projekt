import { CanActivateFn, Router } from '@angular/router';
import { TokenService } from './token.service';
import { inject } from '@angular/core';

export const authGuard: CanActivateFn = (route, state) => {
  return inject(TokenService).authenticated() ? true : inject(Router).createUrlTree(['/auth/login']);
};

export const reverseAuthGuard: CanActivateFn = (route, state) => {
  return inject(TokenService).authenticated() ? inject(Router).createUrlTree(['/']) : true;
}