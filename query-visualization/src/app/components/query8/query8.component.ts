import {Component, OnInit, OnDestroy} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';
import { Subject } from 'rxjs';
import { Data } from '@angular/router';

@Component({
  selector: 'app-query8',
  templateUrl: './query8.component.html',
  styleUrls: ['./query8.component.css']
})
export class Query8Component implements OnInit {

  data_all: any[] = [];
  quarter: string[] = [];
  item: any[] = [];
  dtOptions: DataTables.Settings = {};
  dtTrigger: Subject<any> = new Subject<any>();
  chartOptions: ChartOptions = {
    responsive: true,
    maintainAspectRatio: true,
  };
  constructor(private queryService: QueriesService, private http: HttpClient) {
  }
  ngOnInit() {
    this.dtOptions = {
      pagingType: 'full_numbers',
      pageLength: 2
    };
    this.queryService.getQuery8().subscribe((data:any)=> {
      this.data_all = data;
      this.dtTrigger.next;
    });
  };
  ngOnDestroy(): void {
    this.dtTrigger.unsubscribe();
  }
  // query8Data(): void {
  //   this.queryService.getQuery8().subscribe((data: any) => {
  //       console.log(data);
  //       for(const d of data){
  //         this.quarter.push(d.quarter);
  //         this.item.push(d.item);
  //       }
  //       this.data_all = data;
  //     }
  //   )
  // }
}