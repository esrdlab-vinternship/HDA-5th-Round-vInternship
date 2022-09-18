import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions, ChartType} from "chart.js";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';
import { data } from 'jquery';

@Component({
  selector: 'app-query6',
  templateUrl: './query6.component.html',
  styleUrls: ['./query6.component.css']
})
// export class DemoSearchBar {
  
//   }
export class Query6Component implements OnInit {
  data_all: any[] = [];
  search : String ="";
  constructor(private queryService: QueriesService, private http: HttpClient) {
  }
  ngOnInit() {
    this.query6Data();
  }
  query6Data(): void {
    this.queryService.getQuery6().subscribe((data: any) => {
        console.log(data);

        this.data_all = data;
        console.log(this.data_all)
      }
    )
  }

}