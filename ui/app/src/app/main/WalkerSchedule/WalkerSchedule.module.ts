import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WALKERSCHEDULE_MODULE_DECLARATIONS, WalkerScheduleRoutingModule} from  './WalkerSchedule-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WalkerScheduleRoutingModule
  ],
  declarations: WALKERSCHEDULE_MODULE_DECLARATIONS,
  exports: WALKERSCHEDULE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WalkerScheduleModule { }