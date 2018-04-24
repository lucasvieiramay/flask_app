import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { Observable } from 'rxjs/Observable';

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
      let endpoint = "http://localhost:8080/person/edit/" + objectId;

      return this.http.patch(endpoint, formData).catch(err => {
         alert(err._body);
         return Observable.throw(err._body);
      }).map(response => response.json());
  }

  deletePerson(objectId){
      // TODO: Get this from a enviroment variable
      let endpoint = "http://localhost:8080/person/remove/" + objectId;
      return this.http.delete(endpoint).map(response => response.json());
  }
}
