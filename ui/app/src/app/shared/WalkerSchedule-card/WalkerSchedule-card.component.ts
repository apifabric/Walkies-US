import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkerSchedule-card.component.html',
  styleUrls: ['./WalkerSchedule-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkerSchedule-card]': 'true'
  }
})

export class WalkerScheduleCardComponent {


}