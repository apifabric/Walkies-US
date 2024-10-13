import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OwnerHomeComponent } from './home/Owner-home.component';
import { OwnerNewComponent } from './new/Owner-new.component';
import { OwnerDetailComponent } from './detail/Owner-detail.component';

const routes: Routes = [
  {path: '', component: OwnerHomeComponent},
  { path: 'new', component: OwnerNewComponent },
  { path: ':id', component: OwnerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Owner-detail-permissions'
      }
    }
  },{
    path: ':owner_id/Appointment', loadChildren: () => import('../Appointment/Appointment.module').then(m => m.AppointmentModule),
    data: {
        oPermission: {
            permissionId: 'Appointment-detail-permissions'
        }
    }
},{
    path: ':owner_id/Dog', loadChildren: () => import('../Dog/Dog.module').then(m => m.DogModule),
    data: {
        oPermission: {
            permissionId: 'Dog-detail-permissions'
        }
    }
},{
    path: ':owner_id/Feedback', loadChildren: () => import('../Feedback/Feedback.module').then(m => m.FeedbackModule),
    data: {
        oPermission: {
            permissionId: 'Feedback-detail-permissions'
        }
    }
},{
    path: ':owner_id/Payment', loadChildren: () => import('../Payment/Payment.module').then(m => m.PaymentModule),
    data: {
        oPermission: {
            permissionId: 'Payment-detail-permissions'
        }
    }
},{
    path: ':owner_id/Subscription', loadChildren: () => import('../Subscription/Subscription.module').then(m => m.SubscriptionModule),
    data: {
        oPermission: {
            permissionId: 'Subscription-detail-permissions'
        }
    }
}
];

export const OWNER_MODULE_DECLARATIONS = [
    OwnerHomeComponent,
    OwnerNewComponent,
    OwnerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class OwnerRoutingModule { }