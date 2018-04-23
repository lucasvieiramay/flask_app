import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';

import { DataService } from '../../services/data.service'

@Component({
  selector: 'app-person-detail',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.sass']
})
export class PersonDetailComponent implements OnInit {

  id: string;
  persons = [];
  person = Object;

  constructor(
      private route: ActivatedRoute,
      private dataService: DataService) { }

  ngOnInit() {
    this.id = this.route.snapshot.paramMap.get('id');
    this.dataService.getPersons().subscribe((persons) => {
        for (let key in persons) {
            if (persons.hasOwnProperty(key)) {
                if (key == this.id){
                    this.person = persons[key];
                }
            }
        }
    });
  }
}
