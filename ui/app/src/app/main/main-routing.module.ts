import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Appointment', loadChildren: () => import('./Appointment/Appointment.module').then(m => m.AppointmentModule) },
    
        { path: 'Dog', loadChildren: () => import('./Dog/Dog.module').then(m => m.DogModule) },
    
        { path: 'Feedback', loadChildren: () => import('./Feedback/Feedback.module').then(m => m.FeedbackModule) },
    
        { path: 'Location', loadChildren: () => import('./Location/Location.module').then(m => m.LocationModule) },
    
        { path: 'Owner', loadChildren: () => import('./Owner/Owner.module').then(m => m.OwnerModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'Service', loadChildren: () => import('./Service/Service.module').then(m => m.ServiceModule) },
    
        { path: 'Subscription', loadChildren: () => import('./Subscription/Subscription.module').then(m => m.SubscriptionModule) },
    
        { path: 'Walk', loadChildren: () => import('./Walk/Walk.module').then(m => m.WalkModule) },
    
        { path: 'WalkService', loadChildren: () => import('./WalkService/WalkService.module').then(m => m.WalkServiceModule) },
    
        { path: 'Walker', loadChildren: () => import('./Walker/Walker.module').then(m => m.WalkerModule) },
    
        { path: 'WalkerSchedule', loadChildren: () => import('./WalkerSchedule/WalkerSchedule.module').then(m => m.WalkerScheduleModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }