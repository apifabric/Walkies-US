import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SubscriptionHomeComponent } from './home/Subscription-home.component';
import { SubscriptionNewComponent } from './new/Subscription-new.component';
import { SubscriptionDetailComponent } from './detail/Subscription-detail.component';

const routes: Routes = [
  {path: '', component: SubscriptionHomeComponent},
  { path: 'new', component: SubscriptionNewComponent },
  { path: ':id', component: SubscriptionDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Subscription-detail-permissions'
      }
    }
  }
];

export const SUBSCRIPTION_MODULE_DECLARATIONS = [
    SubscriptionHomeComponent,
    SubscriptionNewComponent,
    SubscriptionDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SubscriptionRoutingModule { }