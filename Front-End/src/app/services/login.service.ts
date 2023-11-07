import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { Login } from '../model/login';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  constructor(private http: HttpClient) { }

  onLogin(username: string, password: string): Observable<Login> {
    const grantType = 'password'; // Set the correct grant type
    const scope = ''; // Set the scope if needed
    const clientId = ''; // Set your client ID
    const clientSecret = ''; // Set your client secret

    // Create form data and append the values
    const formData = new FormData();
    formData.append('grant_type', grantType);
    formData.append('username', username);
    formData.append('password', password);
    formData.append('scope', scope);
    formData.append('client_id', clientId);
    formData.append('client_secret', clientSecret);

    const headers = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.post<Login>('http://localhost:8000/auth/token', formData, { headers }).pipe(
      catchError(this.handleError)
    );    
  }

  getUserInfo(token: string): Observable<Login> {
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    return this.http.get<Login>('http://localhost:8000/auth/user', { headers }).pipe(
      catchError(this.handleError)
    );
  }

  handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      console.error('A client-side or network error occurred:', error.error);
    } else if (error.status === 404) {
      console.error('The requested resource was not found:', error.error);
    } else {
      console.error(`Backend returned code ${error.status}, body was: `, error.error);
    }
    return throwError(() => new Error('Something bad happened; please try again later.'));
  }
}
