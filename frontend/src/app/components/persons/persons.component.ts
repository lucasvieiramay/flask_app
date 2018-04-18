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

}
