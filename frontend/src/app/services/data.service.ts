import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class DataService {
  backendLocation = "http://localhost:8080/"

  constructor(public http:Http) {
  }

  getPersons() {
      let routeBack = 'persons/list';
      console.log(this.backendLocation+routeBack);
      return this.http.get(this.backendLocation+routeBack).map(
        res => res.json())
  }

}
