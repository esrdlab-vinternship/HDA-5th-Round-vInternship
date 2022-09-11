import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';

@Component({
  selector: 'app-query5',
  templateUrl: './query5.component.html',
  styleUrls: ['./query5.component.css']
})
export class Query5Component implements OnInit {

  data_all: any[] = [];
  division: string[] = [];
  total_sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "polarArea",
      label: 'Total sales in Taka',
      data: this.total_sales,
    }
  ];
  chartLabels: string[] = ["Total Sales at division Barisal in 2015"]
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
    this.query5Data();
  }

  query5Data(): void {
    this.queryService.getQuery5().subscribe((data: any) => {
        console.log(data);
        // this.data_all.push(data);
        for(const d of data){
          // console.log(d.division, d.sales);
          // this.division.push(d.division);
          this.total_sales.push(d.total_sales);
        }
        this.data_all = data;
      }
    )
  }

}