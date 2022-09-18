import {Component, OnInit, NgModule} from '@angular/core';
import {ChartDataset, ChartOptions, ChartType} from "chart.js";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';
import { NgChartsModule } from 'ng2-charts';

@Component({
  selector: 'app-query10',
  templateUrl: './query10.component.html',
  styleUrls: ['./query10.component.css']
})
export class Query10Component implements OnInit {
  ngOnInit() {
    this.query10Data();
  }
  query10Data() {
    this.queryService.getQuery10().subscribe((data: any) => {
      console.log(data);
      // this.data_all.push(data);
      for(const d of data){
        // console.log(d.division, d.sales);
        this.store_key.push(d.store_key);
        this.avg_sales.push(d.avg_sales);
        this.month.push(d.month);
      }
      this.data_all = data;
    }
  )}
  data_all: any[] = [];
  store_key: string[] = [];
  month: any[] = [];
  avg_sales: any[] = [];
  public barChartOptions: ChartOptions = {
    responsive: true
  };
  public barChartType: string = 'horizontalBar';
  public barChartLegend = true;

  public barChartData: ChartDataset[] = [
    
    { data: this.avg_sales},
  ]


  public barChartLabels: string[] = this.month;
  public chartClicked({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }

  public chartHovered({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }
  constructor(private queryService: QueriesService, private http: HttpClient) {
  }
}