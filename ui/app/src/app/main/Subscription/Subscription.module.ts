import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SUBSCRIPTION_MODULE_DECLARATIONS, SubscriptionRoutingModule} from  './Subscription-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SubscriptionRoutingModule
  ],
  declarations: SUBSCRIPTION_MODULE_DECLARATIONS,
  exports: SUBSCRIPTION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SubscriptionModule { }