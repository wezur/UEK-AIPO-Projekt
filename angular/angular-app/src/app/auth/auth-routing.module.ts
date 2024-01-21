import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { reverseAuthGuard } from './auth.guard';

const routes: Routes = [
  { path: 'login', component: LoginComponent, canActivate: [reverseAuthGuard] },
  { path: 'register', component: RegisterComponent, canActivate: [reverseAuthGuard] },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AuthRoutingModule {}
