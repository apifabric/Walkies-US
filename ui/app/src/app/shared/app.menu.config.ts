import { MenuRootItem } from 'ontimize-web-ngx';

import { AppointmentCardComponent } from './Appointment-card/Appointment-card.component';

import { DogCardComponent } from './Dog-card/Dog-card.component';

import { FeedbackCardComponent } from './Feedback-card/Feedback-card.component';

import { LocationCardComponent } from './Location-card/Location-card.component';

import { OwnerCardComponent } from './Owner-card/Owner-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';

import { SubscriptionCardComponent } from './Subscription-card/Subscription-card.component';

import { WalkCardComponent } from './Walk-card/Walk-card.component';

import { WalkServiceCardComponent } from './WalkService-card/WalkService-card.component';

import { WalkerCardComponent } from './Walker-card/Walker-card.component';

import { WalkerScheduleCardComponent } from './WalkerSchedule-card/WalkerSchedule-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Appointment', name: 'APPOINTMENT', icon: 'view_list', route: '/main/Appointment' }
    
        ,{ id: 'Dog', name: 'DOG', icon: 'view_list', route: '/main/Dog' }
    
        ,{ id: 'Feedback', name: 'FEEDBACK', icon: 'view_list', route: '/main/Feedback' }
    
        ,{ id: 'Location', name: 'LOCATION', icon: 'view_list', route: '/main/Location' }
    
        ,{ id: 'Owner', name: 'OWNER', icon: 'view_list', route: '/main/Owner' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
        ,{ id: 'Subscription', name: 'SUBSCRIPTION', icon: 'view_list', route: '/main/Subscription' }
    
        ,{ id: 'Walk', name: 'WALK', icon: 'view_list', route: '/main/Walk' }
    
        ,{ id: 'WalkService', name: 'WALKSERVICE', icon: 'view_list', route: '/main/WalkService' }
    
        ,{ id: 'Walker', name: 'WALKER', icon: 'view_list', route: '/main/Walker' }
    
        ,{ id: 'WalkerSchedule', name: 'WALKERSCHEDULE', icon: 'view_list', route: '/main/WalkerSchedule' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AppointmentCardComponent

    ,DogCardComponent

    ,FeedbackCardComponent

    ,LocationCardComponent

    ,OwnerCardComponent

    ,PaymentCardComponent

    ,ServiceCardComponent

    ,SubscriptionCardComponent

    ,WalkCardComponent

    ,WalkServiceCardComponent

    ,WalkerCardComponent

    ,WalkerScheduleCardComponent

];