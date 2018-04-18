import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-persons',
  templateUrl: './persons.component.html',
  styleUrls: ['./persons.component.css']
})

export class PersonsComponent implements OnInit {

    name:string;
    email:string;
    docNum:number;
    birthDate:string;
    avatar:string;


    constructor(private dataService:DataService) {}

  ngOnInit() {
      this.dataService.getPersons().subscribe((persons) => {
          console.log(persons);
      });
  }

}
