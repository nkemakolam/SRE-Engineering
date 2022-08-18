# here would contain all the studies and finding from LFS 261 [SRE]

## Introduction
Do not under estimate the power of a software defects called bug
### Con of outout 
  - cost money
  - Affects lives of millions
  - Cost a company its creditibility
  - lost of customer
  - even death

Contonous delivery was started by Henry Ford in 1915, they started the assembly line for theyr cars assembling and was perfected by toyota production system toyota is owned by Taiichi Ohno 1948 to 1975. All this brought about the whole new word of 
  - Lean 
  - Agile 
  - Just in time delivery 
  - Kanban 
  - Value stream

### Note relaibilty is the most important feature of software delivery
 
  it is possibel to delievery software fast and reliable and that quest is what birthed continous integration.

# Testing is key for  reliable software delivery 
Process in testing
## When sghould you test
run your test when you integrste with the main branch
So what is the sequence of the process for this testing 
## what should you test
## [integrate + build + unitest+ statick checkers + dynamics checkers+ integrtion test+ acceptance test + load lest + compliance test etc]
  - note unit test happen with mock service like mock all more events and all but if you want to test your ciode with real life scenarios then you have to padd your testing with integration test.

Contnous Integration would be defiend as the the process that ensures that any change in your main line of repository goes through enough check[testing] the we are confidence about it reliability

#### Continous ingetration consist of Build + Test[various type of test] + Package and Push to a package managment system like docker

# contnous Deployment 
This is when you go all the way to production with every simple change you make with on the main branch of your repository folloing the sequence of contnous integration with reliability as the watch word.

### Contnous delivery
So what is continous deleivery is where you dont go to production except by a manaul approval by a product manager injecting himself in between staging and production. So the rest of the before process is same just that before production you have to have a manual process of approval  while contnous deployment you go all the way to production without appoval.

## key path/ componenet of  contnous delivery 
  - you must be Agile compliant smaller task and regulry commit
  - build should be automated and fast
  - Testing should be faster and you should consider the pyramid of testing which are desceing order
      - automated unit test
      - automated component test
      - automated service test
      - automated API test
      - automated UI test
  - Deployment should be auto mated with tools eg Azure devops or Octopus deploy

  # Cintinous Delivery Practices
   1. Revision Control this the major stack and has all this varioius componenet 
    -- Application code
    -- Build Logic (Pom.xml, Package.json,makefile)
    -- Configurations
    -- CI Pipepline (eg Jenkinfile or Azure devOps yaml,gitActions yaml)
    -- Artifacts build packaging logics (eg dockerfile)
    -- Infrastructure as Code (eg Ansible shef, puppet, teraform)
    -- Deployment Logics (eg Kubernetes deployment files)
   2. Development Work flow this address your git approach which tests how fast and well your codes are promoted and we have strategies like:
     -- truck based
     -- git flow
     -- gitopd flow
   3. Code review is another important piece of practice code is enhances quality of code that get checked in by adopted the second eye principle and dojo programing and this happens befor the integration to the main brain or repo.
   4. Automated Ci pipelines we Use Jenkins and Azure DevOps to achieve that.
   5. Automated deployment pipelines which handles the deployment of packages into production

#### In summary for continous integration pipeline 
  -- Setup revision control eg git + github
  -- Define workflow and code review
  -- Setup CI platform
  -- Create CI pipeline - Build , Test
  -- Build and manage artefactsn - Packaging jobs
  -- Setup deplyment tools and create deployment Pipelins
