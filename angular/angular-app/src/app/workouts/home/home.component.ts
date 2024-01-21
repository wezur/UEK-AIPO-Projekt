import { Component } from '@angular/core';
import { WorkoutsService } from '../workouts.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  constructor(private workoutsService: WorkoutsService) {
    workoutsService.workoutsList().subscribe({
      next: (v) => {
        console.log(v);
      }
    });
    workoutsService.excercisesList(1).subscribe({
      next: (v) => {
        console.log(v);
      }
    });
   }
}
