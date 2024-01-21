import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable()
export class AuthenticationService {
  private apiUrl = 'http://localhost:80/api';

  constructor(private http: HttpClient) {}

  login(username: string, password: string): Observable<any> {
    const body = { username, password };
    return this.http.post(`${this.apiUrl}/token/`, body);
  }

  refreshToken(token: string): Observable<any> {
    const body = { token };
    return this.http.post(`${this.apiUrl}/token/refresh/`, body);
  }

  register(user: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/register/`, user);
  }
}
