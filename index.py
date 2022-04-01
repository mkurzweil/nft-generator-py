from IPython.display import display
from PIL import Image
import random
import json
import os

os.system('cls' if os.name == 'nt' else 'clear')

# collection name
col_name = "smile#"

def create_new_image(all_images, config):
    new_image = {}
    for layer in config["layers"]:
        new_image[layer["name"]] = random.choices(
            layer["values"], layer["weights"])[0]

    for incomp in config["incompatibilities"]:
        for attr in new_image:
            if new_image[incomp["layer"]] == incomp["value"] and new_image[attr] in incomp["incompatible_with"]:
                return create_new_image(all_images, config)

    if new_image in all_images:
        return create_new_image(all_images, config)
    else:
        return new_image


def generate_unique_images(amount, config):
    print("Generating {} unique NFTs...".format(amount))
    pad_amount = len(str(amount))
    trait_files = {
    }
    for trait in config["layers"]:
        trait_files[trait["name"]] = {}
        for x, key in enumerate(trait["values"]):
            trait_files[trait["name"]][key] = trait["filename"][x]

    all_images = []
    for i in range(amount):
        new_trait_image = create_new_image(all_images, config)
        all_images.append(new_trait_image)

    i = 1
    for item in all_images:
        item["tokenId"] = i
        i += 1

    for i, token in enumerate(all_images):
        attributes = []
        for key in token:
            if key != "tokenId":
                attributes.append({"trait_type": key, "value": token[key]})
        token_metadata = {
            "image": config["baseURI"] + "/images/" + col_name + str(token["tokenId"]) + '.png',
            "tokenId": token["tokenId"],
            "name":  config["name"] + str(token["tokenId"]).zfill(pad_amount),
            "description": config["description"],
            "attributes": attributes
        }
        with open('./metadata/' + str(token["tokenId"]) + '.json', 'w') as outfile:
            json.dump(token_metadata, outfile, indent=4)

    with open('./metadata/all-objects.json', 'w') as outfile:
        json.dump(all_images, outfile, indent=4)

    for item in all_images:
        layers = []
        for index, attr in enumerate(item):
            if attr != 'tokenId':
                layers.append([])
                layers[index] = Image.open(
                    f'{config["layers"][index]["trait_path"]}/{trait_files[attr][item[attr]]}.png').convert('RGBA')

        if len(layers) == 1:
            rgb_im = layers[0].convert('RGB')
            file_name = str(item["tokenId"]) + ".png"
            rgb_im.save("./images/" + col_name + file_name)
        elif len(layers) == 2:
            main_composite = Image.alpha_composite(layers[0], layers[1])
            rgb_im = main_composite.convert('RGB')
            file_name = str(item["tokenId"]) + ".png"
            rgb_im.save("./images/" + col_name + file_name)
        elif len(layers) >= 3:
            main_composite = Image.alpha_composite(layers[0], layers[1])
            layers.pop(0)
            layers.pop(0)
            for index, remaining in enumerate(layers):
                main_composite = Image.alpha_composite(
                    main_composite, remaining)
            rgb_im = main_composite.convert('RGB')
            file_name = str(item["tokenId"]) + ".png"
            rgb_im.save("./images/" + col_name + file_name)

    # v1.0.2 addition
    print("\nUnique NFT's generated. After uploading images to IPFS, please paste the CID below.\nYou may hit ENTER or CTRL+C to quit.")
    cid = input("IPFS Image CID (): ")
    if len(cid) > 0:
        if not cid.startswith("ipfs://"):
            cid = "ipfs://{}".format(cid)
        if cid.endswith("/"):
            cid = cid[:-1]
        for i, item in enumerate(all_images):
            with open('./metadata/' + str(item["tokenId"]) + '.json', 'r') as infile:
                original_json = json.loads(infile.read())
                original_json["image"] = original_json["image"].replace(
                    config["baseURI"]+"/", cid+"/")
                with open('./metadata/' + str(item["tokenId"]) + '.json', 'w') as outfile:
                    json.dump(original_json, outfile, indent=4)


generate_unique_images(100, {
    "layers": [
        {
            "name": "Background",
            "values" : ["Background_0", "Background_1", "Background_2", "Background_3", "Background_4", "Background_5", "Background_6", "Background_7", "Background_8", "Background_9", "Background_10", "Background_11", "Background_12", "Background_13", "Background_14", "Background_15", "Background_16", "Background_17", "Background_18", "Background_19", "Background_20", "Background_21", "Background_22", "Background_23", "Background_24", "Background_25", "Background_26", "Background_27", "Background_28", "Background_29", "Background_30", "Background_31", "Background_32", "Background_33", "Background_34", "Background_35", "Background_36", "Background_37", "Background_38", "Background_39", "Background_40", "Background_41", "Background_42", "Background_43", "Background_44", "Background_45", "Background_46", "Background_47", "Background_48", "Background_49", "Background_50", "Background_51", "Background_52", "Background_53", "Background_54", "Background_55", "Background_56", "Background_57", "Background_58", "Background_59", "Background_60", "Background_61", "Background_62", "Background_63", "Background_64", "Background_65", "Background_66", "Background_67", "Background_68", "Background_69", "Background_70", "Background_71", "Background_72", "Background_73", "Background_74", "Background_75", "Background_76", "Background_77", "Background_78", "Background_79", "Background_80", "Background_81", "Background_82", "Background_83", "Background_84", "Background_85", "Background_86", "Background_87", "Background_88", "Background_89", "Background_90", "Background_91", "Background_92", "Background_93", "Background_94", "Background_95", "Background_96", "Background_97", "Background_98", "Background_99" ],
            "trait_path": "./trait-layers/backgrounds",
            "filename" : ["background_0", "background_1", "background_2", "background_3", "background_4", "background_5", "background_6", "background_7", "background_8", "background_9", "background_10", "background_11", "background_12", "background_13", "background_14", "background_15", "background_16", "background_17", "background_18", "background_19", "background_20", "background_21", "background_22", "background_23", "background_24", "background_25", "background_26", "background_27", "background_28", "background_29", "background_30", "background_31", "background_32", "background_33", "background_34", "background_35", "background_36", "background_37", "background_38", "background_39", "background_40", "background_41", "background_42", "background_43", "background_44", "background_45", "background_46", "background_47", "background_48", "background_49", "background_50", "background_51", "background_52", "background_53", "background_54", "background_55", "background_56", "background_57", "background_58", "background_59", "background_60", "background_61", "background_62", "background_63", "background_64", "background_65", "background_66", "background_67", "background_68", "background_69", "background_70", "background_71", "background_72", "background_73", "background_74", "background_75", "background_76", "background_77", "background_78", "background_79", "background_80", "background_81", "background_82", "background_83", "background_84", "background_85", "background_86", "background_87", "background_88", "background_89", "background_90", "background_91", "background_92", "background_93", "background_94", "background_95", "background_96", "background_97", "background_98", "background_99" ],
            "weights": [69, 58, 42, 82, 43, 10, 56, 30, 12, 80, 69, 31, 48, 82, 42, 66, 23, 42, 41, 38, 42, 76, 60, 74, 89, 50, 54, 44, 55, 11, 31, 36, 77, 23, 54, 79, 59, 64, 88, 76, 40, 34, 32, 82, 78, 27, 39, 71, 31, 37, 61, 89, 65, 17, 48, 60, 43, 86, 86, 54, 10, 52, 31, 50, 47, 34, 20, 71, 44, 14, 66, 41, 33, 38, 49, 38, 26, 82, 58, 36, 21, 78, 80, 59, 86, 51, 51, 10, 39, 18, 42, 56, 14, 32, 45, 73, 39, 69, 53, 60]
            },
        {
            "name": "Foreground",
            "values": ["Smile", "Smile 1"],
            "trait_path": "./trait-layers/foreground",
            "filename": ["smile", "smile"],
            "weights": [50, 50]
        },
        {
            "name": "Branding",
            "values": ["A Name", "Another Name"],
            "trait_path": "./trait-layers/text",
            "filename": ["text", "text"],
            "weights": [50, 50]
        }
    ],
    "incompatibilities": [
        #  {
        #   "layer": "Background",
        #    "value": "Blue",
        #    "incompatible_with": ["Python Logo 2"]
        # },  # @dev : Blue backgrounds will never have the attribute "Python Logo 2".
    ],
    "baseURI": ".",
    "name": "NFT #",
    "description": "This is a description for this NFT series."
})

# Additional layer objects can be added following the above formats. They will automatically be composed along with the rest of the layers as long as they are the same size as eachother.
# Objects are layered starting from 0 and increasing, meaning the front layer will be the last object. (Branding)
