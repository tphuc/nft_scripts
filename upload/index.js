// Import the NFTStorage class and File constructor from the 'nft.storage' package
const{ NFTStorage, File } = require('nft.storage')

// The 'mime' npm package helps us set the correct file type on our File objects
const mime = require('mime')

// The 'fs' builtin module on Node.js provides access to the file system
const fs = require('fs')

// The 'path' module provides helpers for manipulating filesystem paths
const path = require('path')

// Paste your NFT.Storage API key into the quotes:
const NFT_STORAGE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweEY5NDcyOWVkYTg4MWNlMkU1ODI3MWJlMTA1MGIwODkzNDMxMWFCYTIiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY0ODAxNjQ0MjE0NiwibmFtZSI6InByaW1lX3BhdHRlcm4ifQ.vEbMnfQTEBGEWlKyrUk4PB8A4wT1LhAHyhx5xd1uBzM'

/**
  * Reads an image file from `imagePath` and stores an NFT with the given name and description.
  * @param {string} imagePath the path to an image file
  * @param {string} name a name for the NFT
  * @param {string} description a text description for the NFT
  */
async function storeNFT(imagePath, name, description) {
    // load the file from disk
    const image = await fileFromPath(imagePath)

    // create a new NFTStorage client using our API key
    

    // call client.store, passing in the image & metadata
    // const cid = await nftstorage.storeDirectory([
      
    // ])
   
}

/**
  * A helper to read a file from a location on disk and return a File object.
  * Note that this reads the entire file into memory and should not be used for
  * very large files. 
  * @param {string} filePath the path to a file to store
  * @returns {File} a File object containing the file content
  */
async function fileFromPath(filePath) {
    const content = await fs.promises.readFile(filePath)
    const type = mime.getType(filePath)
    return new File([content], path.basename(filePath), { type })
}


/**
 * The main entry point for the script that checks the command line arguments and
 * calls storeNFT.
 * 
 * To simplify the example, we don't do any fancy command line parsing. Just three
 * positional arguments for imagePath, name, and description
 */
async function main() {
    const NftImagesPath = '/Users/phuccoker/NFTs/prime_pattern/images/'
    var filepaths = fs.readdirSync(NftImagesPath);
    console.log(filepaths, filepaths.length)
    var Images = []
    await Promise.all(filepaths.map(async filepath =>  {
        if(filepath.includes('.png')){
            const image = await fileFromPath(NftImagesPath + filepath)
            Images.push(image)
        }
        else {
            console.log('--', filepath)
        }
       
    }))

    console.log(Images.length)
    const nftstorage = new NFTStorage({ token: NFT_STORAGE_KEY })
    
    const cid = await nftstorage.storeDirectory(Images)
    console.log(cid)
   
}

// Don't forget to actually call the main function!
// We can't `await` things at the top level, so this adds
// a .catch() to grab any errors and print them to the console.
main()
 