import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WorkoutsService {
  private apiUrl = 'http://localhost:80/api';

  constructor(private http: HttpClient) {}

  workoutsList(): Observable<any> {
    return this.http.get(`${this.apiUrl}/workouts?start_date=2024-01-16&end_date=2024-01-16`);
  }

  excercisesList(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/exercises?workout_id=${id}`);
  }
}
