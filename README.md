<a href="">
    <img src="https://mblogthumb-phinf.pstatic.net/MjAxODA1MjdfNiAg/MDAxNTI3NDMzMTAwNDY3.31E3jwLoCUnViDVw4iNmeKaj6xoh6NMeI12JkMOifS4g.tGKVTfudBBpqcRDReEREQ5wTVOlRklJ1UKphn12jZXog.PNG.crush_on_ux/14911977598016.png?type=w800" alt="따릉이 로고" title="따릉이" align="right" height="60" />
</a>

서울시 공유 서비스 따릉이 프로세스 개선
======================

<p align="center">
    <img alt="python-3.7.7" src="https://img.shields.io/badge/python-v3.7+-lightgrey?style=flat-square"/>
    <a href="https://www.ksqm.org/" target="_blank">
        <img alt="python-3.7.7" src="https://img.shields.io/badge/prize-KoreaQualitySociety-yellow?style=flat-square"/>
    </a>
    <img alt="build-working" src="https://img.shields.io/badge/docs-87%25-g?style=flat-square"/>
    <img alt="dependencies-up to date" src="https://img.shields.io/badge/dependencies-up to date-g?style=flat-square"/>
    <img alt="license" src="https://img.shields.io/github/license/metterian/redbttn-seoul-studio?style=flat-square"/>
</p>


> 서울시 공유 자전거 따릉이의 어플리케이션 리뷰와 시민의견수렴 게시판의 게시글을 LDA 토픽 모델링 기법을 사용하여 분석한다. 분석된 결과를 O2O 서비스 기준에 맞추어 오프라인 품질과 온라인 품질로 분류 하여 문제점을 제시 한다.

## 소개
- 한국품질경영학회 2019년도 추계 학술 대회, 빅데이터 분야 우수 발표 논문 수상 ([링크](https://drive.google.com/file/d/13-HRrsYMBZvLHYAhLCkqbB5Jq_ULJNc5/view?usp=sharing))
- 최종 발표 자료 ([링크](https://drive.google.com/file/d/114oduD2Uq79Amc4zbarR5ob3HmsPHo-N/view?usp=sharing))

## 프로젝트 프로세스
<p align="center">
    <img src="./image/project_process.png" width="80%" align="middle"/>
</p>

## 방법론
#### 토픽 모델링(LDA)를 통한 어플 리뷰 분석
> LDA(Latent Dirichlet Allocation, 잠재 디리클레 할당) 문서 속에 잠재되어 있는 다양한 주제를 추출하는 분석 기법
1. 불용 단어 제거 후, 명사-형용사-동사 추출
2. Document-Term Matrix 제작
3. 추출된 단어를 토필 모델링(LDA)에 적용함
4. 서로 상관관계가 있는 토픽을 뽑아서 분류



## 분석 결과
### 구글 플레이 어플 리뷰
<p align="center">
    <img src="./image/lda_1.png" width="80%" align="middle"/>
    <img src="./image/lda_2.png" width="80%" align="middle"/>
</p>

### 시민의견수렴 게시판
<p align="center">
    <img src="./image/lda_3.png" width="80%" align="middle"/>
    <img src="./image/lda_4.png" width="80%" align="middle"/>
</p>

### 분석 결론
따릉이 자전거 이용 프로세스 전반적으로 다음과 같은 문제점이 발견되었다.
<p align="center">
    <img src="./image/lda_result.png" width="80%" align="middle"/>
    <img src="./image/process_result.png" width="80%" align="middle"/>
</p>


## License

[![License: LGPL v3](https://img.shields.io/badge/License-MIT-g.svg?style=flat-square)](https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3))

- Copyright © [SeungJun Lee](https://github.com/metterian "matterian").
