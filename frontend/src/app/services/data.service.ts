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
      return this.http.get(this.backendLocation+routeBack).map(
        res => res.json())
  }

  updatePerson(objectId, formData) {
      // TODO: Get this from a enviroment variable
      let endpoint = "http://localhost:8080/person/edit/" + objectId
      console.log(endpoint);
      return this.http.patch(endpoint, formData).map(
          response => response.json())
  }
}
