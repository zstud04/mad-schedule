

class CSEHelper:

    BASE_URL = 'https://enroll.wisc.edu'

    login_selector_1 = 'btn-primary'

    search_selector_1 = 'mat-raised-button'

    course_listings = "//cse-pane[@id='results']/section/section/cse-search-results/div[1]/cse-course-list-item"

    catalog_ref = 'catalog-ref'

    course_title = 'course-title'

    course_description = "//cse-pane[@id='details']/section/section/cse-course-details/section/cse-detail-topic/section/p"
    
    course_details = '//*[@id="details"]/section/section/cse-course-details/section/cse-detail-topic[3]/section/ul'

    subj_notes = '//*[@id="details"]/section/section/cse-course-details/section/cse-detail-topic[4]/section'

    course_section_btn = '//*[@id="details"]/section/section/cse-course-details/section/header/div[2]/button' 

    section_dropdown_btn = '//*[@id="sections"]/section/section/cse-course-packages/cse-detail-topic/section/cse-package-group/details/summary/cse-parent-header/cse-pack-header/div/div[1]/mat-icon[1]'

    section_availability = '//*[@id="sections"]/section/section/cse-course-packages/cse-detail-topic/section/cse-package-group/details/cse-section-details/div[1]/div[1]/cse-detail-topic[1]/section/ul'

    section_back_btn = '//mat-sidenav-container/div'

    next_result_query_btn = '//*[@id="results"]/section/section/cse-search-results/div[2]/button[2]/span[1]/mat-icon'