import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query6',
  templateUrl: './query6.component.html',
  styleUrls: ['./query6.component.css']
})

export class Query6Component implements OnInit {
  data_all: any[] = [];
  store: any[] = [];
  items: any[] = [];


  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query6Data();
  }
  query6Data(): void {
    this.queryService.getQuery6().subscribe((data: any) => {
        console.log(data);
        for (const d of data) {
          //console.log(d.Store, d.Item)
          this.store.push(d.Store)
          this.items.push(d.Item)
        }
      this.data_all = data;
      }
    )
  }

}
