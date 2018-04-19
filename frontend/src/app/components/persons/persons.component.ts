import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-persons',
  templateUrl: './persons.component.html',
  styleUrls: ['./persons.component.css']
})

export class PersonsComponent implements OnInit {

    persons = [];

    constructor(private dataService:DataService) {}

  ngOnInit() {
      this.dataService.getPersons().subscribe((persons) => {
          this.persons = persons;
      });
  }

  getImage(imagePath) {
      if (!imagePath) {
           return "http://localhost:8080/person/image/default.png";
      }
      let correctPath = imagePath.split('/');
      correctPath = correctPath[correctPath.length-1];
      // Join with project url
      // TODO: Get this from a config file
      return "http://localhost:8080/person/image/" + correctPath;
  }

  editProfile(profileId) {
      console.log(profileId);
  }
}
