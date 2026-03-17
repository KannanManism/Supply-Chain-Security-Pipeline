# Chaos Engineering Report
timestamp: 2026-03-17T05:05:07Z
toxiproxy_host: 127.0.0.1
toxiproxy_port: 8474

## SLA Configuration
max_error_rate: 5.0%  # Allow up to 5% errors
max_p95_ms: 1000.0  # 95th percentile response time

## Test Configuration
sample_size: 20 requests per scenario
request_concurrency: 1 concurrent requests
settle_time: 2.0s between scenarios

## Chaos Levels
latency_levels_ms: 50,100,200,400,800
timeout_levels_ms: 50,100,250,500,1000
bandwidth_levels_kbps: 64,128,256,512
packet_limit_bytes: 1,10,50,100
load_levels: 1,5,10,20

## Results

### Baseline (No Chaos)

**No chaos** ✓ PASS  error_rate=0.0% avg=51ms p50=50ms p95=59ms p99=67ms

✓ SLA met for all levels

### Latency Injection

**50ms latency** ✓ PASS  error_rate=0.0% avg=554ms p50=556ms p95=613ms p99=626ms
**100ms latency** ✗ FAIL  error_rate=0.0% avg=1047ms p50=1046ms p95=1124ms p99=1165ms
**200ms latency** ✗ FAIL  error_rate=0.0% avg=2063ms p50=2060ms p95=2088ms p99=2103ms
**400ms latency** ✗ FAIL  error_rate=0.0% avg=4074ms p50=4077ms p95=4113ms p99=4136ms
**800ms latency** ✗ FAIL  error_rate=0.0% avg=8058ms p50=8058ms p95=8102ms p99=8107ms

**Breaking point: 100ms latency**

### Connection Timeouts

**50ms timeout** ✗ FAIL  error_rate=100.0% avg=7419ms p50=7137ms p95=11169ms p99=11587ms
**100ms timeout** ✗ FAIL  error_rate=100.0% avg=7479ms p50=7896ms p95=11040ms p99=11768ms
**250ms timeout** ✗ FAIL  error_rate=100.0% avg=8037ms p50=7525ms p95=11493ms p99=11521ms
**500ms timeout** ✗ FAIL  error_rate=100.0% avg=11171ms p50=11148ms p95=14908ms p99=15433ms
**1000ms timeout** ✗ FAIL  error_rate=100.0% avg=11179ms p50=10476ms p95=15255ms p99=15899ms

**Breaking point: 50ms timeout**

### Bandwidth Throttling

**64kbps** ✓ PASS  error_rate=0.0% avg=66ms p50=66ms p95=70ms p99=71ms
**128kbps** ✓ PASS  error_rate=0.0% avg=56ms p50=56ms p95=61ms p99=66ms
**256kbps** ✓ PASS  error_rate=0.0% avg=58ms p50=58ms p95=64ms p99=64ms
**512kbps** ✓ PASS  error_rate=0.0% avg=54ms p50=52ms p95=65ms p99=69ms

✓ SLA met for all levels

### Packet Loss

**1-byte limit** ✗ FAIL  error_rate=100.0% avg=7516ms p50=7572ms p95=10236ms p99=11222ms
**10-byte limit** ✗ FAIL  error_rate=100.0% avg=1780ms p50=40ms p95=9255ms p99=9422ms
**50-byte limit** ✗ FAIL  error_rate=100.0% avg=34ms p50=31ms p95=43ms p99=47ms
**100-byte limit** ✗ FAIL  error_rate=100.0% avg=31ms p50=32ms p95=34ms p99=36ms

**Breaking point: 1-byte limit**

### Load Testing

**1 concurrent** ✓ PASS  error_rate=0.0% avg=51ms p50=50ms p95=56ms p99=57ms
**5 concurrent** ✓ PASS  error_rate=0.0% avg=64ms p50=59ms p95=89ms p99=91ms
**10 concurrent** ✓ PASS  error_rate=0.0% avg=104ms p50=97ms p95=148ms p99=162ms
**20 concurrent** ✓ PASS  error_rate=0.0% avg=210ms p50=210ms p95=250ms p99=251ms

✓ SLA met for all levels

## Summary

Total scenarios: 23
Passed: 10
Failed: 13

**Result: SLA violations detected**
