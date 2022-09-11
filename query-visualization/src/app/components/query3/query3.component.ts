import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";
import { QueriesService } from 'src/app/services/queries.service';

@Component({
  selector: 'app-query3',
  templateUrl: './query3.component.html',
  styleUrls: ['./query3.component.css']
})
export class Query3Component implements OnInit {

  data_all: any[] = [];
  // division: string[] = [];
  total_sales: any[] = [];

  chartData: ChartDataset[] = [
    {
      type: "doughnut",
      label: 'Total Sales in Barisal',
      data: this.total_sales,
    }
  ];
  chartLabels: string[] = ["Sales in Barisal"]
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
    this.query3Data();
  }

  query3Data(): void {
    this.queryService.getQuery3().subscribe((data: any) => {
        console.log(data);
        // this.data_all.push(data);
        for(const d of data){
          // console.log(d.division, d.total_total_sales);
          // this.division.push(d.division);
          this.total_sales.push(d.total_sales);
        }
        this.data_all = data;
      }
    )
  }

}