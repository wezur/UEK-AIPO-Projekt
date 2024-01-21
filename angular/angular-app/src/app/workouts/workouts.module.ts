import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { WorkoutsRoutingModule } from './workouts-routing.module';
import { MatCardModule } from '@angular/material/card';
import { WorkoutBoxComponent } from './workout-box/workout-box.component';

@NgModule({
  declarations: [HomeComponent, WorkoutBoxComponent],
  imports: [
    CommonModule, WorkoutsRoutingModule, MatCardModule
  ]
})
export class WorkoutsModule { }
