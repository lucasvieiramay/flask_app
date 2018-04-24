import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgForm } from '@angular/forms';
import { DataService } from '../../services/data.service'

@Component({
  selector: 'app-person-detail',
  templateUrl: './person-detail.component.html',
  styleUrls: ['./person-detail.component.css']
})

export class PersonDetailComponent implements OnInit {

  id: string;
  persons = [];
  person = Object;

  constructor(
      private route: ActivatedRoute,
      private router: Router,
      private dataService: DataService) { }

  ngOnInit() {
    this.id = this.route.snapshot.paramMap.get('id');
    this.dataService.getPersons().subscribe((persons) => {
        for (let key in persons) {
            if (persons.hasOwnProperty(key)) {
                if (persons[key]['id'] == this.id){
                    this.person = persons[key];
                }
            }
        }
    });
  }

  deletePerson() {
   if(window.confirm('Are sure you want to delete this item ?')){
       return this.dataService.deletePerson(this.person['id']).subscribe((response) => {
           alert('Person deleted!');
           this.router.navigate(['']);
       });
    }
  }

  submitForm(name, email, doc_id, birth_date) {
    let data = new FormData();
    if (name) {
        data.append('name', name);
    }
    if (email) {
        data.append('email', email);
    }
    if (doc_id) {
        data.append('doc_id', doc_id);
    }
    if (birth_date) {
        data.append('birth_date', birth_date);
    }
    return this.dataService.updatePerson(
      this.person['id'], data).subscribe((response) => {
          alert('Update with Success!');
          this.router.navigate(['']);
    });
  }
}
