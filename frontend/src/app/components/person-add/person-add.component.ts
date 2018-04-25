import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DataService } from '../../services/data.service';
@Component({
  selector: 'app-person-add',
  templateUrl: './person-add.component.html',
  styleUrls: ['./person-add.component.css']
})
export class PersonAddComponent implements OnInit {

    constructor(
        private router: Router,
        private dataService: DataService) { }

  ngOnInit() {
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
    return this.dataService.addPerson(data).subscribe((response) => {
          alert('Person sucessfully created!');
          this.router.navigate(['']);
    });
  }

}
