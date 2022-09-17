import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query2',
  templateUrl: './query2.component.html',
  styleUrls: ['./query2.component.css']
})
export class Query2Component implements OnInit {

  data_all:any[] = [];
  customer_data: string[]  = [];
  sales_data: any[] = [];
  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: 'Sales in Taka',
      data: this.sales_data,
    }
  ];
  chartLabels: string[] = this.customer_data;
  chartOptions: ChartOptions = {
    scales: {
      y: {
        beginAtZero: true
      }
    },

  };
  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.getQuery2Data();
  }

  getQuery2Data(): void{
    this.queryService.getQuery2().subscribe((data:any)=>{
      console.log(data);
      for(const d of data){
        // console.log(d.customer, d.sales)
        this.customer_data.push(d.customer)
        this.sales_data.push(d.sales)
      }
      this.data_all = data;
    })
}

}
