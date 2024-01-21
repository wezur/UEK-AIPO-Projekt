import { Injectable } from '@angular/core';

const TOKEN_KEY = 'UEK-angular-django-auth-token';
const REFRESH_TOKEN_KEY = 'UEK-angular-django-auth-refresh-token';

@Injectable()
export class TokenService {
  authenticated(): boolean {
    return !!this.getToken();
  }

  getToken(): string | null {
    return localStorage.getItem(TOKEN_KEY);
  }

  saveToken(token: string): void {
    localStorage.setItem(TOKEN_KEY, token);
  }

  destroyToken(): void {
    localStorage.removeItem(TOKEN_KEY);
  }

  getRefreshToken(): string | null {
    return localStorage.getItem(REFRESH_TOKEN_KEY);
  }

  saveRefreshToken(token: string): void {
    localStorage.setItem(REFRESH_TOKEN_KEY, token);
  }

  destroyRefreshToken(): void {
    localStorage.removeItem(REFRESH_TOKEN_KEY);
  }
}