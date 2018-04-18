// Angular imports
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HttpModule } from '@angular/http';

// Components imports
import { AppComponent } from './app.component';
import { PersonsComponent } from './components/persons/persons.component';

// Services imports
import { DataService } from './services/data.service';

// Routes config
const appRoutes: Routes = [
  { path: '',      component: PersonsComponent },
];


@NgModule({
  declarations: [
    AppComponent,
    PersonsComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    BrowserModule,
    HttpModule
  ],
  providers: [
    // We manually need to import the services and declare as providers
    DataService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
