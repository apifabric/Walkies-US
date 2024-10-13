import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WalkerSchedule-new',
  templateUrl: './WalkerSchedule-new.component.html',
  styleUrls: ['./WalkerSchedule-new.component.scss']
})
export class WalkerScheduleNewComponent {
  @ViewChild("WalkerScheduleForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}