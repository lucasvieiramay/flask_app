// Angular imports
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// Third part libs
import { ContenteditableDirective } from 'ng-contenteditable';

// Components imports
import { AppComponent } from './app.component';
import { PersonsComponent } from './components/persons/persons.component';
import { PersonDetailComponent } from './components/person-detail/person-detail.component';

// Services imports
import { DataService } from './services/data.service';

// Routes config
const appRoutes: Routes = [
  { path: '',      component: PersonsComponent },
  { path: 'person-detail/:id', component: PersonDetailComponent },
];


@NgModule({
  declarations: [
    AppComponent,
    PersonsComponent,
    ContenteditableDirective,
    PersonDetailComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    BrowserModule,
    HttpModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    // We manually need to import the services and declare as providers
    DataService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
