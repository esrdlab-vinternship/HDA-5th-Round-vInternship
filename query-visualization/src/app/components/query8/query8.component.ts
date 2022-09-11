import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';

@Component({
  selector: 'app-query8',
  templateUrl: './query8.component.html',
  styleUrls: ['./query8.component.css']
})
export class Query8Component implements OnInit {

  data_all: any[] = [];
  quarter: string[] = [];
  item: any[] = [];

  chartData: ChartDataset[] = [
    {   
      type: "bar",
      label: 'Item name',
      data: this.item,
    }
  ];
  chartLabels: string[] = this.quarter
  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    // ⤵️ Remove the grids
    scales: {
      xAxis: {
        display: false,
        grid: {
          drawBorder: false // removes random border at bottom
        }
      },
      yAxis: {
        display: false
      }
    },

    plugins: {
      legend: {
        display: true
      },

      tooltip: {
        // ⤵️ tooltip main styles
        backgroundColor: '#ffeaff',
        displayColors: false, // removes unnecessary legend
        padding: 10,

        // ⤵️ title
        titleColor: '#0b4ad2',
        titleFont: {
          size: 18
        },

        // ⤵️ body
        bodyColor: '#2D2F33',
        bodyFont: {
          size: 13
        }
      }
    }
  };

  constructor(private queryService: QueriesService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query8Data();
  }

  query8Data(): void {
    this.queryService.getQuery8().subscribe((data: any) => {
        console.log(data);
        // this.data_all.push(data);
        for(const d of data){
          // console.log(d.quarter, d.item);
          this.quarter.push(d.quarter);
          this.item.push(d.item);
        }
        this.data_all = data;
      }
    )
  }

}