import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Subscription-card.component.html',
  styleUrls: ['./Subscription-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Subscription-card]': 'true'
  }
})

export class SubscriptionCardComponent {


}