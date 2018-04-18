import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { PersonsComponent } from './components/persons/persons.component';
import { DataService } from './services/data.service';

@NgModule({
  declarations: [
    AppComponent,
    PersonsComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [
    // We manually need to import the services and declare as providers
    DataService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
