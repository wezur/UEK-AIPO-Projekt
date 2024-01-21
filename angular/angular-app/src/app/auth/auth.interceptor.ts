import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpClient
} from '@angular/common/http';
import { Observable, catchError } from 'rxjs';
import { TokenService } from './token.service';
import { Router } from '@angular/router';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(private tokenService: TokenService, private router: Router, private http: HttpClient) {}

  intercept(
    request: HttpRequest<unknown>,
    next: HttpHandler
  ): Observable<HttpEvent<unknown>> {
    const token = this.tokenService.getToken();

    if (token) {
      request = request.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`,
        },
      });
    }

    return next.handle(request).pipe(
      catchError((error) => {
        if (error.status === 401 && request.url !== 'http://localhost:80/api/token/refresh/') {
          this.tokenService.destroyToken();
          let body = { refresh: this.tokenService.getRefreshToken() };
          this.http.post('http://localhost:80/api/token/refresh/', body).subscribe({
            next: (v: any) => {
              this.tokenService.saveToken(v.access),
              request = request.clone({
                setHeaders: {
                  Authorization: `Bearer ${v.access}`,
                },
              });
              return next.handle(request);
            },
            error: (e) => {
              this.router.navigate(['/auth/login']);
            }
          });
        }
        throw error;
      })
    );
  }
}
