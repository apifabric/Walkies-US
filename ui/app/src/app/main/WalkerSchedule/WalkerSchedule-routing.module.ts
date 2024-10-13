import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkerScheduleHomeComponent } from './home/WalkerSchedule-home.component';
import { WalkerScheduleNewComponent } from './new/WalkerSchedule-new.component';
import { WalkerScheduleDetailComponent } from './detail/WalkerSchedule-detail.component';

const routes: Routes = [
  {path: '', component: WalkerScheduleHomeComponent},
  { path: 'new', component: WalkerScheduleNewComponent },
  { path: ':id', component: WalkerScheduleDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkerSchedule-detail-permissions'
      }
    }
  },{
    path: ':schedule_id/Appointment', loadChildren: () => import('../Appointment/Appointment.module').then(m => m.AppointmentModule),
    data: {
        oPermission: {
            permissionId: 'Appointment-detail-permissions'
        }
    }
}
];

export const WALKERSCHEDULE_MODULE_DECLARATIONS = [
    WalkerScheduleHomeComponent,
    WalkerScheduleNewComponent,
    WalkerScheduleDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkerScheduleRoutingModule { }