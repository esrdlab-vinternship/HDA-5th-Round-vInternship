import {Component, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-query7',
  templateUrl: './query7.component.html',
  styleUrls: ['./query7.component.css']
})
export class Query7Component implements OnInit {

  private days_input: any;
  query7Form = new FormGroup({
    days: new FormControl('')
  });

  constructor(private queryService: QueriesService) {
  }
  data_all: any[] = [];
  dtOptions: DataTables.Settings = {};
  ngOnInit() {
    this.dtOptions = {
      pagingType: 'full_numbers'
    };
  }

  search(){
    this.days_input = this.query7Form.value.days
    this.queryService.getQuery7(this.days_input).subscribe((data:any)=>{
      console.log(data);
      this.data_all = data;
    })
  }

}